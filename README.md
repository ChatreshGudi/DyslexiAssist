# DyslexiAssist: AI For Dyslexia

## Overview
AI For Dyslexia is an AI-powered tool designed to assist individuals with dyslexia by improving text readability, correcting letter reversals, enhancing word recognition, and providing adaptive reading support. This project leverages machine learning, OpenCV, and AI-driven text processing to make reading more accessible and comfortable for dyslexic users.
![image](./Screenshots/Home.png)
## Features
- **Letter Reversal & Orientation Correction**: Uses OCR and AI post-processing to identify and correct reversed letters.
- **AI-Driven Color Overlays & Background Adjustments**: Implements OpenCV for customizable color filters to enhance readability.
- **AI-Powered Text Customization**: Adjusts letter spacing and highlights phonetics for better word differentiation.
- **AI-Based Screen Adjustments**: Utilizes webcam-based eye-tracking to dynamically adjust text positioning.
- **AI-Powered Phonetic Correction**: Integrates LanguageTool API for advanced spelling, grammar, and phonetic corrections.
- **AI Summary & Questioning System**: Uses GPT-based AI to summarize text and generate comprehension questions.
- **Adaptive Contrast Testing System**: Dynamically adjusts contrast based on user feedback, response time, and eye-tracking data.
![image](./Screenshots/Contrast%20Test.png)

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- pyttsx3
- speech_recongition
- Google Cloud Vision API
- Gemini API (for AI-based text corrections and summarization)

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/ChatreshGudi/AI_For_Dyslexia.git
   cd AI_For_Dyslexia
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the program:
   ```sh
   python main.py
   ```

## Usage
- The program provides various AI-powered tools to assist with reading difficulties.
- Users can customize settings such as font, color overlays, and spacing based on their preferences.
- The adaptive contrast testing system helps refine readability dynamically.

## Contributors
- **[Rithvik A M](https://github.com/Rithvik2006)**
- **[Chatresh Ramasai Gudi](https://github.com/ChatreshGudi)** 
- **[Arvind Kothamangala](https://github.com/Nightly1177)**
- **[Aamer Khan](https://github.com/aamer236)**

## License
This project is open-source and available under the MIT License.

## Acknowledgments
- OpenAI for GPT-based text processing.
- LanguageTool API for phonetic and grammatical corrections.
- OpenCV for image processing and enhancements.
- Matplotlib for visualization support.

For more details, visit the [GitHub Repository](https://github.com/ChatreshGudi/AI_For_Dyslexia).

