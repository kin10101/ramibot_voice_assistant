import json


def add_intent():
    # Load existing intents file
    with open('intents.json') as f:
        intents = json.load(f)

    # Get input for new intent
    tag = input("Enter tag for new intent: ")
    patterns = input("Enter patterns for new intent (separated by commas): ").split(',')
    responses = input("Enter responses for new intent (separated by |): ").split('|')

    # Add new intent to intents file
    intents['intents'].append({
        "tag": tag,
        "patterns": patterns,
        "responses": responses
    })

    # Save updated intents file
    with open('intents.json', 'w') as f:
        json.dump(intents, f, indent=4)


def display_json(filename):
    with open(filename) as f:
        data = json.load(f)
        print(json.dumps(data, indent=4))


def edit_intent(filename, intent_name, new_responses):
    with open(filename, 'r') as f:
        data = json.load(f)

    # Find the intent in the data
    for intent in data['intents']:
        if intent['tag'] == intent_name:
            intent['responses'] = new_responses
            break

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
