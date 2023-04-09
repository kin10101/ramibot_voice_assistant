import time
import sys
import speech_recognition as sr
import pyttsx3
import random

import chatbot

# Define the wake word and list of variations
WAKE_WORD = "hello rami"
WAKE_WORD_VARIATIONS = [
    "hello ram",
    "hello mommy",
    "hello romy",
    "hello run",
    "hello robi",
    "hiram",
]

# Initialize text-to-speech engine
engine = pyttsx3.init()


# Define function to speak text out loud
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Initialize chatbot
# ...

def listen_for_command():
    """
    Listens for a voice command and returns the recognized text.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please try again.")
    except sr.RequestError:
        speak("Sorry, there was an error processing your request. Please try again later.")

    return None


def handle_command(text):
    """
    Handles the given voice command and returns the chatbot response.
    """
    if text == "stop":
        speak("Goodbye!")
        sys.exit()
    elif text is not None:
        response = chatbot.handle_request(text)
        if response is not None:
            return response
        else:
            speak("Sorry, I'm not sure how to respond to that.")
    return None


def test_assistant():
    while True:
        print("Speak now...")
        text = listen_for_command()
        if text is None:
            continue

        if any(variation in text for variation in WAKE_WORD_VARIATIONS):
            speak("I'm listening.")
            command_text = listen_for_command()
            response_text = handle_command(command_text)
            if response_text is not None:
                speak(response_text)


test_assistant()
