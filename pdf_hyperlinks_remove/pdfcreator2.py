from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

pdf_path = "demo.pdf"

input_pdf = PdfFileReader(pdf_path)

# input_pdf = input_pdf.removeLinks()
# for j in range(0, len(input_pdf['/Annots'])):
#     writer_annot = input_pdf['/Annots'][j].getObject()
#     for field in data_dict: 
#         if writer_annot.get('/T') == field:
#             writer_annot.update({
#                 NameObject("/Ff"): NumberObject(1)   # make ReadOnly
#             })

pdf_writer = PdfFileWriter()

pdf_writer.appendPagesFromReader(input_pdf)

with Path("demo_r.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

