#necessary modules
import cv2
import pytesseract
import os
import re

#path to tessract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#extract text from image and draw a green box around it
def extract_text_and_draw_box(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)
    _, thresh_frame = cv2.threshold(blur_frame, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    data = pytesseract.image_to_data(thresh_frame, output_type=pytesseract.Output.DICT)
    
    extracted_text = ""
    
    for i in range(len(data['text'])):
        x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
        text = data['text'][i]
        if text.strip() != "":
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            extracted_text += text + " "
    
    return frame, extracted_text.strip()

def wrap_text(text, max_line_length):
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= max_line_length:
            if current_line != "":
                current_line += " "
            current_line += word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return lines

if __name__ == "__main__":
    #camera capture
    cap = cv2.VideoCapture(0) # 0 is default cam
    
    # save captures in folders (create one if not existant)
    output_folder = r"C:\Users\User\Desktop\images"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    while True:
        ret, frame = cap.read()
        processed_frame, extracted_text = extract_text_and_draw_box(frame)
        
        #display extracted text on camera window
        if extracted_text:
            max_line_length = 30
            wrapped_text = wrap_text(extracted_text, max_line_length)
            text_y = 50
            for line in wrapped_text:
                cv2.putText(processed_frame, line, (50, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                text_y += 30
            
            print("Extracted text:")
            print(extracted_text)
            filename = re.sub(r'[^a-zA-Z0-9\s]', '_', extracted_text)
            filename = os.path.join(output_folder, filename + ".png")
            cv2.imwrite(filename, processed_frame)
        
        cv2.imshow('Real-Time Text Reading', processed_frame)
        
       #press q to exit loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    #close windows
    cap.release()
    cv2.destroyAllWindows()