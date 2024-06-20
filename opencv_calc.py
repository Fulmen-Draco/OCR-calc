import cv2
import pytesseract
import re
import streamlit as st
from PIL import Image
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
# Function to preprocess the image and extract text using pytesseract
def extract_text_from_image(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to preprocess the image
    #_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    
    # Use pytesseract to extract text
    extracted_text = pytesseract.image_to_string(gray)
    
    return extracted_text

# Function to find mathematical equations in extracted text
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

# Function to format the equation (handle implied multiplication)
def format_equation(equation):
    # Insert multiplication operator where a number is directly followed by a parenthesis
    equation = re.sub(r'(\d)(\()', r'\1*\2', equation)
    return equation

# Function to solve the equation
def solve_equation(equation):
    try:
        # Evaluate the equation using eval
        result = eval(equation)
        return result
    except Exception as e:
        return str(e)

# Main function to orchestrate the OCR process
def main(image):
    # Extract text from the image using pytesseract and OpenCV
    text = extract_text_from_image(image)
    st.write(f"Extracted Text: {text}")
    
    # Find the equation in the extracted text
    equation = find_equation(text)
    if equation:
        st.write(f"Extracted Equation: {equation}")
        
        # Format the equation to handle implied multiplication
        formatted_equation = format_equation(equation)
        st.write(f"Formatted Equation: {formatted_equation}")
        
        # Solve the equation
        result = solve_equation(formatted_equation)
        st.write(f"Result: {result}")
    else:
        st.write("No equation found in the image.")

# Streamlit interface
st.title("OCR Calculator with OpenCV and Tesseract")
uploaded_file = st.file_uploader(label="Upload an image", type=['jpg', 'png', 'jpeg'])
if uploaded_file:
    image = Image.open(uploaded_file)
    image_np = np.array(image)
    main(image_np)
