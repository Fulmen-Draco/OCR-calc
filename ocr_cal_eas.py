import cv2
import easyocr
import re
import streamlit as st

def extract_text_from_image(image_path):
    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en'])
    
    # Read the image
    image = cv2.imread(image_path)
    
    # Use EasyOCR to extract text
    result = reader.readtext(image, detail=0)
    
    # Join the results into a single string
    extracted_text = ' '.join(result)
    
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


image_path = 'C:/Users/KIIT/Desktop/projects-nlp/equ.jpg'
main(image_path)
