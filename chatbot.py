import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import load_model

import command_functions
import texttospeech as tts

# Load data
lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
print(words) #------------
classes = pickle.load(open('classes.pkl', 'rb'))
print(classes)
model = load_model('chatbot_model.h5')

# Get dict command mappings
intent_methods = command_functions.command_mappings

#get data from database and return it
def get_from_database():
    """Get data from database."""

    pass
def clean_up_sentence(sentence):
    """Tokenize and lemmatize the sentence."""
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]

    # --------------------------------------------------------------------------
    print("clean up sentence output", sentence_words)
    # --------------------------------------------------------------------------
    return sentence_words


def bag_of_words(sentence):
    """Create a bag of words from the sentence."""
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1

    # ---------------------------------------------------------------------------
    print("bag of words output", np.array(bag))
    # --------------------------------------------------------------------------
    return np.array(bag)


def predict_class(sentence):
    """Predict the intent of the sentence."""
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.5  # Acceptable limit adjust in testing
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)  # sort by strength of probability
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})  # remove strings

    # ---------------------------------------------------------------------------
    print("predict_class output", return_list)
    # --------------------------------------------------------------------------
    return return_list


def get_response(intents_list, intents_json, context):
    """Get a response based on the predicted intent."""
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    result = None
    for i in list_of_intents:
        print(i)
        if i['tag'] == tag:

            if 'context_filter' in i and i['context_filter'] not in context:
                result = "blocked by context filters"
                continue
            if 'context_set' in i:  # set context
                context[0] = i['context_set']

            if 'function' in i:
                print("FOUND FUNCTION! DO SOMETHING")

            result = random.choice(i['responses'])  # Gets a random response from the given list
            break
    # ---------------------------------------------------------------------------
    print("get response output", result)
    # --------------------------------------------------------------------------
    return result


def handle_request(message, context):
    """Determine whether the predicted intent corresponds to a custom command function
    or a standard response and return the appropriate output."""
    predicted_intents = predict_class(message)
    check_response = get_response(predicted_intents, intents, context)

    if not predicted_intents:
        response = "sorry, I am not yet capable of responding to that"

    elif predicted_intents[0]['intent'] in intent_methods.keys():  # if predicted intent is mapped to a function
        intent_methods[predicted_intents[0]['intent']]()

    else:
        response = check_response

    # ---------------------------------------------------------------------------
    print("get request output", response)
    # --------------------------------------------------------------------------
    return response


def get_tag(message):
    tag = predict_class(message)
    return tag


def test_chatbot():
    """Test chatbot by using the command line."""
    context = [""]
    while True:
        print(context)

        try:
            message = input("")  # get input
            # predict = predict_class(message)
            # response = get_response(predict, intents)  # get response from get_response()
            response = handle_request(message, context)  # get response from request()

            if response:
                tts.speak(response)  # Text to speech function
                print(response)  # output response in terminal

        except Exception as e:
            response = e
            pass
