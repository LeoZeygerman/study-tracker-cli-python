from subject_logic import show_all, completed, special_show

def study_menu():
    while True:
        try:
            print('1.Посмотреть предметы')
            print('2.Отмеить выполнение')
            print('3.Изменить предмет')
            print('4.Выход')
            choice = int(input('Ваш выбор: '))
            
            if choice == 1:
                special_show()
                
            if choice == 2:
                completed()
            
        except ValueError:
            print('Ошибка при вводе!')