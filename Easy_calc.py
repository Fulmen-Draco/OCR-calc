import cv2
import easyocr
import re
import streamlit as st
from PIL import Image
import numpy as np


def extract_text_from_image(image):
    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en'])
    # Convert the image to a format readable by OpenCV
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    result = reader.readtext(image, detail=0)
    # Join the results into a single string
    extracted_text = ' '.join(result)
    return extracted_text

def find_equation(text):
    # find all instances of arithmetic expressions
    equation_pattern = re.compile(r'[\d\+\-\*\/\(\)\s]+')
    matches = equation_pattern.findall(text)
    # Join the matches to form the equation string
    if matches:
        equation = ''.join(matches)
        return equation
    else:
        return None

def format_equation(equation):
    # Inserting multiplication operator where a number is directly followed by a parenthesis
    equation = re.sub(r'(\d)(\()', r'\1*\2', equation)
    return equation

def solve_equation(equation):
    try:
        result = eval(equation)
        return result
    except Exception as e:
        return str(e)

def main(image):
    text = extract_text_from_image(image)
    st.write(f"Extracted Text from image: {text}")
    equation = find_equation(text)
    if equation:
        st.write(f"Extracted Equation: {equation}")
        formatted_equation = format_equation(equation)
        st.write(f"Formatted Equation: {formatted_equation}")
        result = solve_equation(formatted_equation)
        st.write(f"Result: {result}")
    else:
        st.write("No equation found in the image.")

# Streamlit interface
st.title("OCR Calculator")
uploaded_file = st.file_uploader(label="Upload an image", type=['jpg', 'png', 'jpeg'])
if uploaded_file:
    image = Image.open(uploaded_file)
    main(image)
