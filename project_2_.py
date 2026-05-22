import pyttsx3
engine=pyttsx3.init()
engine.say("Can I ask your lovely name? ")
engine.runAndWait()

while True:
   user_question=input("Can I ask your lovely name? :")

   if user_question=="Yes".lower():
    a=input("Thanks, What is your name :")
    print(f"Nice to meet you {a}")
    engine.say(f"nice to meet you{a} ")
    engine.runAndWait()

   elif user_question=="No".lower():
    engine.say("Ok good bye, have a nice day")
    engine.runAndWait()

   elif user_question=="hello" or "hye" or "hii":
     print("Hye"or "Hello")

   else:
     print("I can't recognize this word.")





