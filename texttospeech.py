# text to speech config module
import pyttsx3

voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enCA_RichardM"
#voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_JA-JP_HARUKA_11.0'
engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('rate', 200)
engine.setProperty('voice', voice_id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def getvoices():
    """prints out a list of available voices"""
    voices = engine.getProperty('voices')

    for voice in voices:
        # to get the info. about various voices in our PC
        print("Voice:")
        print("ID: %s" % voice.id)
        print("Name: %s" % voice.name)
        print("Age: %s" % voice.age)
        print("Gender: %s" % voice.gender)
        print("Languages Known: %s" % voice.languages)

getvoices()