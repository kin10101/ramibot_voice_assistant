import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from keras.models import load_model

import command_functions
import texttospeech as tts

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')

# get dict command mappings
intent_methods = command_functions.command_mappings
# intent_methods = json.loads(open('intent_methods.json').read()) # doesnt work


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.5  # acceptable limit adjust in testing

    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
        print(str(r[1]))
    return return_list


def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    result = None
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            # gets a random response from the given list
            break
    return result


def request(message):
    #  determine whether the predicted intent corresponds to a custom command function
    #  or a standard response and returns the appropriate output.
    ints = predict_class(message)

    if ints[0]['intent'] in intent_methods.keys():  # ints[0]['intent'] is tag in intents.json
        intent_methods[ints[0]['intent']]()
    else:
        talk = True
        return get_response(ints, intents)


def get_tag(message):
    ints = predict_class(message)
    return ints


def test_chatbot():  # output variable is response, input variable is message. for speech input set message as mic input
    while True:

        try:
            message = input("")  # get input
            ints = predict_class(message)  # scan for keywords?
            response = request(message)

            if response:
                tts.speak(response)  # Text to speech function
                print(response)  # response
                print("tag triggered: " + ints[0]['intent'])
        except Exception as e:
            response = e
            pass
