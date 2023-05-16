import speech_recognition as sr
r = sr.Recognizer()


def get_audio():
    with sr.Microphone() as source:  # audio listener config
        r.energy_threshold = 10000
        #r.adjust_for_ambient_noise(source, 1.5)
        audio = r.listen(source)
    return audio


def audiototext(audio):
    text = r.recognize_google(audio)  # converts audio to text
    return text.lower()

