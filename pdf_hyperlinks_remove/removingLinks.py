
import PyPDF2

# This works fine
with open('demo.pdf', 'rb') as pdf_obj:
    pdf = PyPDF2.PdfFileReader(pdf_obj)
    out = PyPDF2.PdfFileWriter()
    for page in pdf.pages:
        # page.scale(2, 2)

        extracted = page.extractText()
        
        print(extracted, "\n\n")
        out.addPage(page)
        
    with open('new.pdf', 'wb') as f: 
        out.removeLinks()
        dir(out)
        out.write(f)

# # This attempts to remove annotations
# with open('old.pdf', 'rb') as pdf_obj:
#     pdf = PyPDF2.PdfFileReader(pdf_obj)
#     page = pdf.pages[2]
#     print(page['/Annots'], '\n\n\n\n')
#     page.Annots = []
#     print(page['/Annots'])