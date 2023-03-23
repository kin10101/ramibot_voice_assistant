import speech_recognition


def print_live():
    recognizer = speech_recognition.Recognizer()
    while True:
        try:
            with speech_recognition.Microphone as source:
                recognizer.adjust_for_ambient_noise(source, duration=.2)
                audio = recognizer.listen(source)

                text = recognizer.recognize_google(audio)
                text = text.lower()

                print(f"Recognized {text}")

        except speech_recognition.UnknownValueError():
            recognizer = speech_recognition.Recognizer()
            continue


print_live()
