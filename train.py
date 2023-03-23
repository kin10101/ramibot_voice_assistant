import json
import pickle
import string
import random
import numpy as np
import texttospeech as tts

import nltk
from nltk.stem import WordNetLemmatizer  # It has the ability to lemmatize.

import tensorflow as tensorF  # A multidimensional array of elements is represented by this symbol.
from keras import Sequential  # Sequential groups a linear stack of layers into a tf.keras.Model
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

nltk.download("punkt")  # required package for tokenization
nltk.download("wordnet")  # word database

lemmatizer = WordNetLemmatizer()  # for getting words

intents = json.loads(open('intents.json').read())

# lists
words = []
classes = []
documents = []
ignore_letters = ['!', '?', '.', ',']

# Each intent is tokenized into words and the patterns and their associated tags are added to their respective lists.
for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        word_list = nltk.word_tokenize(pattern)  # tokenize the patterns
        words.extend(word_list)  # extends the tokens
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words))

classes = sorted(set(classes))

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))
# print(words) #see lemmatized data

training = []
output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training, dtype=object)

train_x = list(training[:, 0])
train_y = list(training[:, 1])

# initialize training model
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save('chatbot_model.h5', hist)

print('done training')
tts.speak('training is complete.')