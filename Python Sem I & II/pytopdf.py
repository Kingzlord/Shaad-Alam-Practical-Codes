from reportlab.platypus import SimpleDocTemplate, Preformatted
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from tkinter import Tk, filedialog
import os

# ===== OUTPUT FOLDER =====
output_folder = r"D:\My folder\Study\Python\Pdf"

# Create folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Hide tkinter root window
Tk().withdraw()

# Select MULTIPLE files
input_files = filedialog.askopenfilenames(
    title="Select files to convert",
    filetypes=[
        ("All files", "*.*"),
        ("Python files", "*.py"),
        ("Jupyter notebooks", "*.ipynb"),
        ("Text files", "*.txt")
    ]
)

if not input_files:
    print("No files selected")
    exit()

styles = getSampleStyleSheet()

for file_path in input_files:
    # Create PDF name in output folder
    file_name = os.path.basename(file_path)
    base_name = os.path.splitext(file_name)[0]
    pdf_file = os.path.join(output_folder, base_name + ".pdf")

    # Read file safely
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    # Build PDF
    doc = SimpleDocTemplate(pdf_file, pagesize=A4)
    content = [Preformatted(text, styles["Code"])]
    doc.build(content)

    print("Created:", pdf_file)

print("\nAll files converted successfully 🚀")
