# Real-Time Text Reader with OpenCV and Tesseract

This Python script allows you to extract and display text from live camera feed in real-time. By using OpenCV and Tesseract OCR, it provides an easy way to process text directly from your webcam or other camera sources.

## How to run and functions used:

**Installation**: Make sure you have the required libraries installed. You can install them using pip:
```
pip install opencv-python pytesseract
```

**Setup Tesseract**: Set the path to the Tesseract OCR executable in the script.
```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe
```
**Text Extraction and Box Drawing**: The script captures frames from the camera feed and extracts text using Tesseract OCR. It highlights detected text regions with green boxes on the video feed.

**Output Image Saving**: If text is extracted, the script saves the processed frame with the extracted text overlaid as an image file in the specified output folder.

## Examples:
![(Extended)](https://github.com/Jadsabbagh/Real-Time-Text-Reader-Opencv/assets/164062104/0638f5ec-23b2-41e7-a6d6-58d80265d922)
![arthur miller dearh ofa salesman](https://github.com/Jadsabbagh/Real-Time-Text-Reader-Opencv/assets/164062104/dbc19448-5c9b-4b43-8ac0-b68d8ed41676)

## Inaccuracy Considerations
It's essential to acknowledge that the accuracy of text extraction may vary based on factors such as lighting conditions, camera quality, and text complexity. Tesseract OCR, while powerful, may not always provide 100% accurate results, especially with handwritten or distorted text. Therefore, it's recommended to verify extracted text for accuracy and consider implementing additional preprocessing techniques or using alternative OCR engines for improved results, depending on your application's requirements.
![Inaccuracy](https://github.com/Jadsabbagh/Real-Time-Text-Reader-Opencv/assets/164062104/325d8aca-3383-48b2-b509-8dfb0ab6ab5c)
