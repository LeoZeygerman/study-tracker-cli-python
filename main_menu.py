from subject_logic import add_subject
def main_menu():
    while True:
        try:
            
            print('1.Добавить предмет')
            print('2.Посмотреть ваши предметы')
            print('3.Перейти в меню предметов')
            print('4.Выйти')
            choice = int(input('Ваш выбор: '))
            
            if choice == 1:
                add_subject()
            
        except ValueError:
            print('Ошибка при вводе!')