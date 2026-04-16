# 📄 Smart Document Scanner + OCR

A Python-based **Smart Document Scanner** that converts PDF pages into clean scanned black-and-white images and extracts text using **OCR**.

This project combines:
- **PyMuPDF (`fitz`)** → PDF page reading
- **OpenCV (`cv2`)** → image preprocessing and thresholding
- **PyTesseract** → text extraction (OCR)
- **NumPy** → image array handling

It works like a mini **CamScanner + OCR Reader**.

---

# 🚀 Features
- 📄 Read multi-page PDF files
- 🖼 Convert PDF pages to images
- 🎯 Convert image to grayscale
- 🧹 Remove noise using Gaussian Blur
- ✨ Apply adaptive thresholding for scanner effect
- 🔍 Extract text from scanned pages using OCR
- 💾 Save extracted text into `output.txt`
- 👀 Display scanned pages in a window

---

# 🛠 Technologies Used
- Python 3.x
- OpenCV
- PyMuPDF
- NumPy
- PyTesseract
- Tesseract OCR Engine

---

# 📦 Installation
Install required libraries:

```bash
pip install opencv-python numpy pymupdf pytesseract
```

Also install **Tesseract OCR** on Windows.

Default path:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

---

# ▶️ Project Code
```python
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

    with open("output.txt", "a", encoding="utf-8") as file:
        file.write(f"\n--- Page {i+1} ---\n")
        file.write(text)

    cv.imshow(f"Page {i+1}", scanned)
    cv.waitKey(0)

cv.destroyAllWindows()
```

---

# ⚙️ Working Flow
```text
PDF File
   ↓
Convert page to image
   ↓
Grayscale conversion
   ↓
Gaussian blur
   ↓
Adaptive thresholding
   ↓
OCR text extraction
   ↓
Save text file
```

---

# 🧠 Use Cases
- Resume scanner
- Notes scanner
- PDF text extractor
- Document digitization
- OCR preprocessing
- Smart archive system

---

# 🚀 Future Improvements
- 📑 Export scanned pages as PDF
- 🧠 NLP-based resume parser
- 🔎 Keyword search in extracted text
- 📊 Skill extraction from resumes
- 🌐 Flask web app interface
- ☁️ Cloud OCR API integration

---

# 👨‍💻 Author
**Soham Ghag (Bit-Coder)**

AI • OpenCV • OCR • NLP Projects

