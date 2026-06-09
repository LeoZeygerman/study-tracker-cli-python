from subject_logic import show_all, completed, special_show, change_subject, delete_subject

def study_menu():
    while True:
        try:
            print('1.Посмотреть предметы')
            print('2.Отметить выполнение')
            print('3.Изменить предмет')
            print('4.Удалить предмет')
            print('5.Выход в главное меню')
            print('6.Выход')
            choice = int(input('Ваш выбор: '))
            
            if choice == 1:
                special_show()
                
            if choice == 2:
                completed()
                
            if choice == 3:
                change_subject()
            
            if choice == 4:
                delete_subject()
                
            if choice == 5:
                return 'main'
                
            if choice == 6:
                exit()
            
        except ValueError:
            print('Ошибка при вводе!')