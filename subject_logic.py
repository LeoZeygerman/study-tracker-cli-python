from storage import save_data, load_data

def add_subject():
    name = input('Введите название предмета: ')
    day_time = int(input('Введите количество минут в день: '))
    target = input('Введите цель изучения этого предмета: ')
    data = load_data()
    subject = {
        'name': name,
        'day_time': day_time,
        'target': target
    }
    data.append(subject)
    save_data(data)