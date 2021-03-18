from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

pdf_path = "demo.pdf"

input_pdf = PdfFileReader(pdf_path)

pdf_writer = PdfFileWriter()

num_of_original_pages = input_pdf.getNumPages()

for n in range(0,num_of_original_pages):
    page = input_pdf.getPage(n)

    # work on the page
    # print(page)
    
    print(page.__dict__)
    print(page.removeLinks
    # print(page.extractText())


 



    pdf_writer.addPage(page)

print(pdf_writer.getNumPages())

with Path("demo_slice_1.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)