from kivy.clock import Clock
import os
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.text import LabelBase
from kivy.config import Config
from chatbot import handle_request

os.environ['MESA_LOADER_DRIVER_OVERRIDE'] = 'i965 ./kiwix-desktop'

Window.size = (500, 600)
Config.set('graphics', 'borderless', 1) # 0 being off 1 being on as in true/false

class ChatBubble(MDLabel):
    pass


class ChatScreen(Screen):
    pass


class Command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()

    font_size = 17


class Response(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()

    font_size = 17


class ChatBot(MDApp):
    input_text = ""

    def change_screen(self, screen_name):
        screen_manager.current = screen_name

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file('ChatbotGUI.kv'))
        return screen_manager

    def send_message(self):
        global size, halign, value

        # Get the text from the text input
        self.input_text = screen_manager.get_screen("ChatGUI").text_input.text.strip()

        # Check if the input text is not empty
        if self.input_text:
            value = self.input_text
            if len(value) < 6:
                size = .22
                halign = "center"
            elif len(value) < 11:
                size = .32
                halign = "center"
            elif len(value) < 16:
                size = .45
                halign = "center"
            elif len(value) < 21:
                size = .58
                halign = "center"
            elif len(value) < 26:
                size = .71
                halign = "center"
            else:
                size = .85
                halign = "left"

            # Add the message to the chat list
            screen_manager.get_screen("ChatGUI").chat_list.add_widget(Command(text=value, size_hint_x=size, halign=halign))
        # Clear the text input
        screen_manager.get_screen("ChatGUI").text_input.text = ""
        self.get_text_input()
        self.response()

        # Now you can use the input_text variable outside of this function
    def get_text_input(self):
        print("Input text:", self.input_text)



    def response(self, *args):
        response = ""
        context = [""]
        response = handle_request(self.input_text.lower(), context)
        # if response is not None:
        #     screen_manager.get_screen("ChatGUI").chat_list.add_widget(
        #         Response(text=response, size_hint_x=.75, halign=halign))
        # else:
        #     # Handle the case where the response is None (e.g., no valid response from the chatbot)
        #     screen_manager.get_screen("ChatGUI").chat_list.add_widget(
        #         Response(text="I'm sorry, I couldn't understand that.", size_hint_x=.75, halign=halign))

        screen_manager.get_screen("ChatGUI").chat_list.add_widget(Response(text=response, size_hint_x=.75, halign=halign))




if __name__ == '__main__':
    LabelBase.register(name='Poppins', fn_regular="GUI/Assets/Poppins-Regular.otf")  # font for chat bubbles
    ChatBot().run()
