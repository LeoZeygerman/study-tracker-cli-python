from storage import save_data, load_data
from models import Subject

def add_subject():
    name = input('Введите название предмета: ')
    day_time = int(input('Введите количество минут в день: '))
    target = input('Введите цель изучения этого предмета: ')
    data = load_data()
    subject = {
        'name': name,
        'day_time': day_time,
        'target': target,
        'last_complete': None,
        'complete': None
    }
    data.append(subject)
    save_data(data)
    for item in data:
        subject_object = Subject(item['name'], item['day_time'], item['target'], item['last_complete'], item['complete'])
    subject_object.get_info()
    
def show_all():
    data = load_data()
    for item in data:
        subject_object = Subject(item['name'], item['day_time'], item['target'], item['last_complete'], item['complete'])
        subject_object.get_info()
    
def completed():
    data = load_data()
    choice = input('Введите название предмета, который хотите отметить: ')
    for item in data:
        if choice.lower() == item['name'].lower(): 
            subject_object = Subject(item['name'], item['day_time'], item['target'], item['last_complete'], item['complete'])
            subject_object.completed()
            item['last_complete'] = subject_object.last_completed
            item['complete'] = subject_object.complete
            save_data(data)
            subject_object.add_completed()
            item['last_complete'] = subject_object.last_completed
            item['complete'] = subject_object.complete
            save_data(data)