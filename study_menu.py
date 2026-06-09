

def study_menu():
    while True:
        try:
            print('1.Посмотреть предметы')
            print('2.Отмеить выполнение')
            print('3.Изменить предмет')
            print('4.Выход')
            choice = int(input('Ваш выбор: '))
        except ValueError:
            print('Ошибка при вводе!')