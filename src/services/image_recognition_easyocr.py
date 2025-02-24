import io
import contextlib
import easyocr
from typing import Optional, Tuple

class ImageRecognitionService:
    """Service class for handling image text recognition using EasyOCR."""
    
    def __init__(self, languages: Optional[list] = None):
        """Initialize the image recognition service.
        
        Args:
            languages (list): List of languages to be used by EasyOCR
        """
        self.languages = languages if languages else ['en']
        self.reader = easyocr.Reader(self.languages)

    def detect_document(self, path: str) -> Tuple[str, Optional[str]]:
        """Detect and extract text from an image document.
        
        Args:
            path (str): Path to the image file
            
        Returns:
            Tuple[str, Optional[str]]: Tuple containing (extracted_text, error_message)
                If successful, error_message will be None
                If failed, extracted_text will be empty and error_message will contain the error
        """
        try:
            # Perform text detection
            result = self.reader.readtext(path, detail=0)
            if not result:
                return "", "No text detected in the image"
            
            # Join the detected text into a single string
            extracted_text = " ".join(result)
            return extracted_text, None

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
            # Perform text detection with confidence scores
            result = self.reader.readtext(path, detail=1)
            if not result:
                return "", 0.0, "No text detected in the image"
            
            # Extract text and calculate average confidence
            extracted_text = " ".join([text for _, text, _ in result])
            confidences = [conf for _, _, conf in result]
            average_confidence = sum(confidences) / len(confidences) if confidences else 0.0
            
            return extracted_text, average_confidence, None

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
        reader = easyocr.Reader(['en'])

        try:
            result = reader.readtext(path, detail=0)
            if not result:
                print("No text detected in the image")
                return output.getvalue()
            
            extracted_text = " ".join(result)
            print(extracted_text)
        except Exception as e:
            print(f"Error processing image: {e}")
            return output.getvalue()
    return extracted_text