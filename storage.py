import json

def load_data():
    try:
        with open('data/subject.json', 'r') as f:
            return json.load(f)
    except ValueError:
        return []
    
def save_data(data):
    with open('data/subject.json', 'w') as f:
        json.dump(data, f)