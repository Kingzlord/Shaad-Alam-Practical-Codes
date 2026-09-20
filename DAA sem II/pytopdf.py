from reportlab.platypus import SimpleDocTemplate, Preformatted
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from tkinter import Tk, filedialog
import os

# Hide the tkinter window
Tk().withdraw()

# Open file picker for .py file
py_file = filedialog.askopenfilename(
    title="Select Python file",
    filetypes=[("Python files", "*.py")]
)

# If user cancels
if not py_file:
    print("No file selected")
    exit()

# Auto-create PDF in same folder
pdf_file = os.path.splitext(py_file)[0] + ".pdf"

# Read code
with open(py_file, "r") as f:
    code = f.read()

# Create PDF
doc = SimpleDocTemplate(pdf_file, pagesize=A4)
styles = getSampleStyleSheet()
content = [Preformatted(code, styles["Code"])]

doc.build(content)

print("PDF created at:", pdf_file)
