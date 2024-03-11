from pypdf import PdfWriter
import os

merger = PdfWriter()
# files = [file for file in os.listdir("E:\Local\Documents\C Programming\Python") if file.endswith(".pdf")]
dict = "E:\Local\Documents"
files = [file for file in os.listdir(dict) if file.endswith(".pdf")]  
for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()