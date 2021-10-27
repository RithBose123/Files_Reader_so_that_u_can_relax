import pyttsx3
import PyPDF2
file_to_be_read=input("File to be read= ")
book= open(file_to_be_read,"rb")
pdfReader=PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
speaker=pyttsx3.init()


for num in range(0,pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()