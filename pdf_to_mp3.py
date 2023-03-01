# pip install PyPDF3 pyttsx3 pdfplumber
import PyPDF3
import pyttsx3
import pdfplumber

file = '/Users/emmaolsen/Library/CloudStorage/OneDrive-Aarhusuniversitet/python_projects_freetime/pdf_to_mp3/AnalogicalReasoning.pdf'

# create a file object for the PDF file and a PDF reader object
book = open(file, 'rb')
pdfReader = PyPDF3.PdfFileReader(book)

# find total number of pages
pages = pdfReader.numPages

# extract text from PDF file
finalText = ""
with pdfplumber.open(file) as pdf:
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        finalText += text
        
        
engine = pyttsx3.init()
engine.save_to_file(finalText, '/Users/emmaolsen/Library/CloudStorage/OneDrive-Aarhusuniversitet/python_projects_freetime/pdf_to_mp3/AnalogicalReasoning.mp3')
engine.runAndWait()
