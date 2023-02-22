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


def get_date():
    today = datetime.date.today()
    current_day = today.strftime("%B %d")
    tts.speak("it is currently " + current_day)


# convert to a json file afterwards
command_mappings = {
    "test_func": test_func,
    "sing": sing,
    "current_time": get_time
}
