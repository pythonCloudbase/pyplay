from PyPDF2 import PdfFileReader

pdf_reader = PdfFileReader("demo.pdf")

print(pdf_reader.documentInfo)


pdf_page = pdf_reader.getPage(0)

pdf_page.extractText()

# for page in pdf_reader.pages:
#       print(page.extractText())

# Creating a new PDF file

# from PyPDF2 import PdfFileWriter

# pdf_writer = PdfFileWriter()

# pdf_writer.addBlackPage