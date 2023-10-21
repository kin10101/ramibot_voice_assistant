import pyttsx3

engine = pyttsx3.init("espeak")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[11].id)  # English


def speak(text):
    engine.say(text)
    engine.runAndWait()


speak("Hello, I am a text-to-speech engine in Python.")
