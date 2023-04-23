import playaudio
import texttospeech as tts
import datetime
from datetime import datetime
import addintent
import train

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


def add_intents():
    # add new intents to the intents.json file
    addintent.add_intent()

    pass

def train_bot():
    # train the bot with the new intents
    train.trainBot()
    pass

# convert to a json file afterwards


command_mappings = {
    "test_func": test_func,
    "sing": sing,
    "current_time": get_time,
    "current_date": get_date,
    "add_intents": add_intents,
    "update": train_bot
}
