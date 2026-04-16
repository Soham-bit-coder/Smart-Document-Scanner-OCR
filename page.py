import fitz
import cv2 as cv
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pdf = fitz.open("opencv\\soham_resume.pdf")

for i in range(len(pdf)):
    page = pdf[i]

    matrix = fitz.Matrix(2, 2)
    pix = page.get_pixmap(matrix=matrix)

    img = np.frombuffer(pix.samples, dtype=np.uint8)
    img = img.reshape(pix.height, pix.width, pix.n)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    gray = cv.GaussianBlur(gray, (5, 5), 0)

    scanned = cv.adaptiveThreshold(
        gray,
        255,
        cv.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv.THRESH_BINARY,
        15,
        5
    )

    text = pytesseract.image_to_string(scanned)
    print(text)

    with open("output.txt", "a", encoding="utf-8") as file:
        file.write(text)
