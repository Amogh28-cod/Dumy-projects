# installing module
import pyttsx3
import PyPDF2

# taking name of file
PDF=input("Enter file name (Make sure it is in the folder):")

# opening the file
Pdf_FIle=open(PDF,'rb')

# reading it by PyPDF
Pdf_Reader=PyPDF2.PdfReader(Pdf_FIle)

# creating a page
text=''
for page in Pdf_Reader.pages:
    text+=page.extract_text()
    print(text) #printing file's line 

# voice command
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()