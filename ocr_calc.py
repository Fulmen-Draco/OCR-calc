import cv2
import pytesseract
import re

# Ensure Tesseract is installed and pytesseract is configured correctly
# You can install tesseract-ocr on your system and then provide the path if needed:
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

def extract_text_from_image(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Use pytesseract to extract text
    extracted_text = pytesseract.image_to_string(gray)
    
    return extracted_text

def find_equation(text):
    # Clean the text to find the equation part
    # This regex will capture equations with parentheses and basic arithmetic operations
    equation_pattern = re.compile(r'[\d\+\-\*\/\(\)\s]+')
    matches = equation_pattern.findall(text)
    
    # Join the matches to form the equation string
    if matches:
        equation = ''.join(matches)
        return equation
    else:
        return None
    

def solve_equation(equation):
    try:
        # Evaluate the equation using eval
        result = eval(equation)
        return result
    except Exception as e:
        return str(e)

def main(image_path):
    # Extract text from the image
    text = extract_text_from_image(image_path)
    print(f"Extracted Text: {text}")
    
    # Find the equation in the extracted text
    equation = find_equation(text)
    if equation:
        print(f"Extracted Equation: {equation}")
        
        # Solve the equation
        result = solve_equation(equation)
        print(f"Result: {result}")
    else:
        print("No equation found in the image.")

# Example usage
image_path = 'C:/Users/KIIT/Desktop/projects-nlp/equ.jpg'
main(image_path)
