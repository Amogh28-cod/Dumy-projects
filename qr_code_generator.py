import qrcode
import pyttsx3

engine=pyttsx3.init()

# get user data

data=input("Enter your Data :")

# generating qr code 

img=qrcode.make(data)

# saving Image of qr code

img.save('Qrcode.png')

# Alert to user

print("Your image is saved as 'Qrcode.png', Please check it in the folder", \
"Thanks")

# Voice command

engine.say("Your image is saved as 'Qrcode.png', Please check it in the folder", \
"Thanks")
engine.runAndWait()