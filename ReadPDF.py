#############################################################################################
###Program Name: ReadPDF.py
###Programmer: Aaliyah Raderberg
###Project: Working with PDF Documents
#############################################################################################
###Working with PDF Documents
##PdfReader is used instead of PdfFileReader.
##len(pdf_reader.pages) is used to get the number of pages in the PDF.
##pdf_reader.pages[page_num] is used to access individual pages.
##page.extract_text() is used to extract text from each page.
 
import PyPDF2

def pdf_to_text(input_pdf, output_txt):
    with open(input_pdf, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)

        text = ""
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    with open(output_txt, "w", encoding="utf-8") as text_file:
        text_file.write(text)

input_pdf = "Django.pdf"
output_txt = "output_pdf2.txt"
pdf_to_text(input_pdf, output_txt)
