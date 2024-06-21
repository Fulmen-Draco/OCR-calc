# OCR Calculator with Streamlit and EasyOCR

This project implements an OCR-based calculator using Streamlit for the interface and EasyOCR for text extraction. The project evolves through three main stages, demonstrating the development from a basic script to a full-featured web application.

## Table of Contents
- [Libraries](#libraries)
- [Project Overview](#project-overview)
- [Files and Iterations](#files-and-iterations)
  - [ocr_cal_eas.py](#ocr_cal_easpy)
  - [Easy_calc.py](#easy_calcpy)
  - [Easy_calc_canvas.py](#easy_calc_canvaspy)
- [Usage](#usage)
- [Installation](#installation)

## Libraries
Ensure you have the following libraries installed:
- easyocr
- opencv-python
- numpy
- streamlit
- streamlit-drawable-canvas

You can install these using pip:
```sh
pip install easyocr opencv-python numpy streamlit streamlit-drawable-canvas
```
or use the requirements.txt:
```sh
pip install -r requirements.txt
```

## Project Overview
The project is built in an iterative manner, enhancing functionality with each step:
1. **Initial Script (ocr_cal_eas.py)**: Basic script that reads an image from a path, extracts text, finds an equation, and solves it.
2. **Web Interface (Easy_calc.py)**: Extends the script to allow image uploads through a Streamlit web interface.
3. **Canvas Drawing (Easy_calc_canvas.py)**: Adds a drawable canvas in the Streamlit interface, allowing users to draw equations directly.

## Files and Iterations

### ocr_cal_eas.py
This is the initial script that processes an image from a given path:
- **extract_text_from_image**: Reads an image file, uses EasyOCR to extract text.
- **find_equation**: Uses regex to find an arithmetic equation in the extracted text.
- **solve_equation**: Solves the extracted equation using Python's `eval` function.
- **main**: Orchestrates the extraction, equation finding, and solving process.

### Easy_calc.py
This iteration introduces a Streamlit web interface where users can upload an image:
- Modified **extract_text_from_image** to handle Streamlit image uploads.
- The Streamlit interface allows image uploads, processes the image, and displays the extracted text, equation, and result.

### Easy_calc_canvas.py
The final iteration enhances the web interface by adding a drawable canvas:
- Users can draw equations on the canvas.
- **format_equation**: New function to handle formatting issues in equations (e.g., inserting multiplication signs).
- The Streamlit interface includes a canvas for drawing, and a button to solve the drawn equation.

## Usage

### Running the Application
1. **ocr_cal_eas.py**:
   ```sh
   python ocr_cal_eas.py
   ```
   Pass the image path to the `main` function to see the extracted text and the result.

2. **Easy_calc.py**:
   ```sh
   streamlit run Easy_calc.py
   ```
   Upload an image through the Streamlit interface to see the extracted text and the result.

3. **Easy_calc_canvas.py**:
   ```sh
   streamlit run Easy_calc_canvas.py
   ```
   Draw an equation on the canvas, then click "Solve" to see the result.
