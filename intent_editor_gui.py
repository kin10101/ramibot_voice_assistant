import json
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import train
import chatbot


class IntentEditor(BoxLayout):
    def __init__(self, intents, **kwargs):
        super().__init__(**kwargs)
        self.intents = intents
        self.intent_list.adapter.data = [i['tag'] for i in intents['intents']]

    def search(self, tag):
        self.current_intent = None
        for i in self.intents['intents']:
            if i['tag'] == tag:
                self.current_intent = i
                break
        if self.current_intent:
            self.response_input.text = self.current_intent['responses'][0]
        else:
            self.response_input.text = ''

    def save(self, response):
        if self.current_intent:
            self.current_intent['responses'][0] = response
            with open('intents.json', 'w') as f:
                json.dump(self.intents, f, indent=4)

class IntentEditorApp(App):
    def build(self):
        with open('intents.json', 'r') as f:
            intents = json.load(f)
        return IntentEditor(intents=intents)

if __name__ == '__main__':
    IntentEditorApp().run()