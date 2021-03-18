from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

pdf_path = "demo.pdf"

input_pdf = PdfFileReader(pdf_path)

input_pdf = input_pdf.removeLinks()



pdf_writer = PdfFileWriter()

pdf_writer.appendPagesFromReader(pdf_reader)

with Path("demo_r.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)