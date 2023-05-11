import chatbot
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


def train_bot():
    running = bool
    # train the bot with the new intents
    train.train_bot()
    print("please restart for the changes to take effect")
    return running is False


# convert to a json file afterwards
def restart():
    chatbot.test_chatbot()


def display_intents():
    addintent.display_json("intents.json")


def edit_intent():
    intent_tag = input("Enter the tag of the intent you want to edit: ")
    new_responses = input("Enter new responses for the intent (separated by commas): ").split(',')
    addintent.edit_intent("intents.json", intent_tag, new_responses)


command_mappings = {
    "test_func": test_func,
    "sing": sing,
    "current_time": get_time,
    "current_date": get_date,
    "add_intents": add_intents,
    "update": train_bot,
    "restart": restart,
    "display_intents": display_intents
}
