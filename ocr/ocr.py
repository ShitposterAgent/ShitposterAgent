
import pytesseract
from PIL import Image

def analyze_screenshot(image_path: str) -> str:
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text