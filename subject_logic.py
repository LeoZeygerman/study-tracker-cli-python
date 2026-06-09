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
        'complete': 'Не отмечен'
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
        
def special_show():
    data = load_data()
    for item in data:
        subject_object = Subject(item['name'], item['day_time'], item['target'], item['last_complete'], item['complete'])
        subject_object.full_show()
    
def completed():
    data = load_data()
    choice = input('Введите название предмета, который хотите отметить: ')
    word = None
    for item in data:
        word = item['name']
        if choice.lower() == word.lower(): 
            subject_object = Subject(item['name'], item['day_time'], item['target'], item['last_complete'], item['complete'])
            subject_object.completed()
            item['last_complete'] = subject_object.last_completed
            item['complete'] = subject_object.complete
            save_data(data)
            subject_object.add_completed()
            item['last_complete'] = subject_object.last_completed
            item['complete'] = subject_object.complete
            save_data(data)
            subject_object.full_show()
            
            
def change_subject():
    data = load_data()
    print('1.Изменить название предмета')
    print('2.Изменить время изучения предмета')
    print('3.Изменить цель предмета')
    choice = int(input('Ваш выбор: '))
    if choice == 1:
        old_name = input('Введите старое название предмета: ')
        word = None
        for item in data:
            word = item['name']
            if old_name.lower() == word.lower():
                new_name = input('Введите новое название: ')
                item['name'] = new_name
                save_data(data)
                subject_object = Subject(item['name'], item['day_time'], item['target'], item['last_complete'], item['complete'])
                subject_object.get_info()
    if choice == 2:
        name = input('Введите название предмета, у которого хотите изменить время: ')
        word = None
        for item in data:
            word = item['name']
            if name.lower() == word.lower():
                new_time = int(input('Введите новое количество минут: '))
                item['day_time'] = new_time
                save_data(data)
                subject_object = Subject(item['name'], item['day_time'], item['target'], item['last_complete'], item['complete'])
                subject_object.get_info()
                
    if choice == 3:
        name = input('Введите название предмета, у которого хотите изменить цель: ')
        word = None
        for item in data:
            word = item['name']
            if name.lower() == word.lower():
                new_target = input('Введите новую цель: ')
                item['target'] = new_target
                save_data(data)
                subject_object = Subject(item['name'], item['day_time'], item['target'], item['last_complete'], item['complete'])
                subject_object.get_info()
                
                
def delete_subject():
    data = load_data()
    name = input('Введите название предмета, который хотите удалить: ')
    word = None
    for item in data:
        word = item['name']
        if name.lower() == word.lower():
            data.remove(item)
            save_data(data)
            print('Предмет успешно удален!')