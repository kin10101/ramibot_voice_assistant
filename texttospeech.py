# text to speech config module
import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('rate', 200)
engine.setProperty('voice', voices[1].id)


# 0 for male voice 1 for female voice

def speak(text):
    engine.say(text)
    engine.runAndWait()
