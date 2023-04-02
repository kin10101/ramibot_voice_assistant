import playaudio
import texttospeech as tts
import datetime
from datetime import datetime


def sing():
    print("singing")
    playaudio.play(playaudio.song)


def test_func():
    print("running function")
    pass


def get_time():
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    tts.speak("it is currently " + current_time)
    print("")


def get_date():
    now = datetime.now()
    current_day = now.strftime("%A %B %d")
    day_of_week = now.strftime("%A")
    tts.speak("Today is " + current_day)


# convert to a json file afterwards

command_mappings = {
    "test_func": test_func,
    "sing": sing,
    "current_time": get_time,
    "current_date": get_date
}
