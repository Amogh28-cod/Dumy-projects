from googletrans import Translator
import pyttsx3

engine=pyttsx3.init()

translator = Translator()

# Get user input
while True:
    text_to_translate = input("Enter text to translate: ")
    target_language = input("Enter target language code : ")

# Translate the text
    translated_text = translator.translate(text_to_translate, dest=target_language)

# Display the result
    print(f"Translated Text: {translated_text.text}")
    engine.say(f"Translated Text: {translated_text.text}")
    engine.runAndWait()
    
    