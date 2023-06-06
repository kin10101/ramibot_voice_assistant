import sys

import speech_recognition as sr

import chatbot
import texttospeech as ts
from playaudio import wakeSound, endSound
from playaudio import play

WAKE_WORD = 'hello rami'
WAKE_WORD_VARIATIONS = [
    "hello ram",
    "hello mommy",
    "hello romy",
    "hello run",
    "hello robi",
    "hello ron",
    "hiram",
    "hey rami",
    "rami",
    "hey ronnie",

]


def handle_command(text, context):  # has bugs
    try:
        if text is not None:
            response = chatbot.handle_request(text, context)
            if response is not None:
                return response
    except:
        print("unknown word")
        # ts.speak("I currently don't know how to respond to that")
        pass


def get_wake_word():
    with sr.Microphone() as source:
        r = sr.Recognizer()
        r.pause_threshold = 0.8
        r.energy_threshold = 10000
        r.dynamic_energy_threshold = True
        audio = r.listen(source)
        text = r.recognize_google(audio)
        return text.lower()


def test_assistant():
    while True:
        try:
            print('speak now')

            # record audio from microphone
            with sr.Microphone() as source:
                r = sr.Recognizer()
                r.pause_threshold = 0.8
                r.energy_threshold = 10000
                r.operation_timeout = 5000
                r.dynamic_energy_threshold = True

                audio = r.listen(source)
                print("listening now")

                # transcribe audio input

                text = r.recognize_google(audio)
                text = text.lower()
                print("wake-word received text: " + text)

                # check wake word
                if any(variation in text for variation in WAKE_WORD_VARIATIONS):
                    print('now listening')
                    play(wakeSound)

                    # listen for the command after wake word is detected
                    audio = r.listen(source)
                    text = r.recognize_google(audio)
                    text = text.lower()
                    print("Received command: " + text)

                    context = []
                    # generate a response from the chatbot
                    response = handle_command(text, context)
                    if response:
                        ts.speak(response)

                    ints = chatbot.get_tag(text)
                    try:
                        print("tag triggered: " + ints[0]['intent'])
                    except:

                        pass

        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service")
        except sr.UnknownValueError:
            print("Unable to recognize speech")
        except sr.WaitTimeoutError:
            print("Timeout error while waiting for speech input")
        except KeyboardInterrupt:
            ts.speak('bye')
            ts.engine.stop()
            sys.exit()


test_assistant()
