import cv2
from PIL import Image
import pytesseract

# Path to your installed Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\saket\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def detect_text(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

if __name__ == "__main__":
    image_path = 'hitman.jpg'
    try:
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Image not found or unable to load.")

        # Show the image
        cv2.imshow("Image", img)

        # Detect and print text
        detected_text = detect_text(image_path)
        print("Detected Text:")
        print(detected_text)

        # Wait and close windows
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"Error: {e}")

