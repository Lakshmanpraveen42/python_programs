from gtts import gTTS
from playsound import playsound

audio = 'speech.mp3'
language = 'en'

text = input("Enter text which you want to convert in to speech: ")

sp = gTTS(text=text, lang=language, slow=False)
sp.save(audio)
playsound(audio)

