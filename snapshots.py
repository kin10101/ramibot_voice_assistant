
def run_assistant():
    while True:
        try:
            print('speak now')
            with sr.Microphone() as source:
                r = sr.Recognizer()
                r.pause_threshold = 0.8
                r.energy_threshold = 10000
                # r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source)
                print(audio)

                text = r.recognize_google(audio)
                text = text.lower()
                print(text)

                # check for wake word
                if any(variation in text for variation in WAKE_WORD_VARIATIONS):
                    print('now listening')

                    play(louder_sound)

                    audio = r.listen(source)
                    text = r.recognize_google(audio)
                    text = text.lower()
                    print(text)

                    if text == 'stop':
                        ts.speak('bye')
                        ts.engine.stop()
                        sys.exit()

                    else:
                        if text is not None:
                            response = chatbot.request(text)
                            if response is not None:
                                ts.speak(response)
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
