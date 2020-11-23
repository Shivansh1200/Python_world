
import pyttsx3
import PyPDF2

book=open('python_tutorial.pdf', 'rb')
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)
spaeker=pyttsx3.init()
for num in range(9, pages):
    starting_page=pdfReader.getPage(10)
    text=starting_page.extractText()
    #spaeker.say(text)
    #spaeker.say('Good evening Shivaansh, How are you. I hope you are doing great and keeping safe. well, I am your personal assistant, Jaarvis')
    spaeker.runAndWait()