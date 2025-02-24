import io
import contextlib
from google.cloud import vision
from typing import Optional, Tuple

class ImageRecognitionService:
    """Service class for handling image text recognition using Google Cloud Vision API."""
    
    def __init__(self, credentials_path: str = "steady-datum-451003-c7-7ef478384fc5.json"):
        """Initialize the image recognition service.
        
        Args:
            credentials_path (str): Path to Google Cloud credentials JSON file
        """
        self.credentials_path = credentials_path
        self._client = None

    @property
    def client(self) -> vision.ImageAnnotatorClient:
        """Lazy initialization of Vision client."""
        if self._client is None:
            self._client = vision.ImageAnnotatorClient.from_service_account_file(self.credentials_path)
        return self._client

    def detect_document(self, path: str) -> Tuple[str, Optional[str]]:
        """Detect and extract text from an image document.
        
        Args:
            path (str): Path to the image file
            
        Returns:
            Tuple[str, Optional[str]]: Tuple containing (extracted_text, error_message)
                If successful, error_message will be None
                If failed, extracted_text will be empty and error_message will contain the error
        """
        output = io.StringIO()
        
        try:
            # Read image file
            with open(path, "rb") as image_file:
                content = image_file.read()
        except Exception as e:
            return "", f"Error opening file: {e}"

        try:
            # Create image object and perform text detection
            image = vision.Image(content=content)
            response = self.client.document_text_detection(image=image)
            
            # Check for errors in the response
            if response.error.message:
                return "", f"Error from Vision API: {response.error.message}"

            # Extract text annotations
            texts = response.text_annotations
            if not texts:
                return "", "No text detected in the image"

            # Return the full text description from the first annotation
            return texts[0].description, None

        except Exception as e:
            return "", f"Error processing image: {e}"

    def detect_document_with_confidence(self, path: str) -> Tuple[str, float, Optional[str]]:
        """Detect text from document with confidence score.
        
        Args:
            path (str): Path to the image file
            
        Returns:
            Tuple[str, float, Optional[str]]: Tuple containing (extracted_text, confidence, error_message)
                confidence will be between 0 and 1
                If failed, extracted_text will be empty, confidence will be 0, and error_message will contain the error
        """
        try:
            with open(path, "rb") as image_file:
                content = image_file.read()

            image = vision.Image(content=content)
            response = self.client.document_text_detection(image=image)

            if response.error.message:
                return "", 0.0, f"Error from Vision API: {response.error.message}"

            # Calculate average confidence across all pages
            confidence = 0.0
            page_count = 0
            
            for page in response.full_text_annotation.pages:
                page_confidence = 0.0
                word_count = 0
                
                for block in page.blocks:
                    for paragraph in block.paragraphs:
                        for word in paragraph.words:
                            word_confidence = sum(symbol.confidence for symbol in word.symbols) / len(word.symbols)
                            page_confidence += word_confidence
                            word_count += 1
                
                if word_count > 0:
                    confidence += page_confidence / word_count
                    page_count += 1

            final_confidence = confidence / page_count if page_count > 0 else 0.0
            
            return response.text_annotations[0].description if response.text_annotations else "", final_confidence, None

        except Exception as e:
            return "", 0.0, f"Error processing image: {e}"

    def is_supported_format(self, file_path: str) -> bool:
        """Check if the file format is supported.
        
        Args:
            file_path (str): Path to the image file
            
        Returns:
            bool: True if the format is supported, False otherwise
        """
        supported_formats = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.ico'}
        return any(file_path.lower().endswith(fmt) for fmt in supported_formats)

def detect_document(path):
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        client = vision.ImageAnnotatorClient.from_service_account_file("steady-datum-451003-c7-7ef478384fc5.json")

        try:
            with open(path, "rb") as image_file:
                content = image_file.read()
        except Exception as e:
            print(f"Error opening file: {e}")
            return output.getvalue()

        image = vision.Image(content=content)

        response = client.document_text_detection(image=image)
        texts = response.text_annotations
        print(texts[0].description)
    return texts[0].description 