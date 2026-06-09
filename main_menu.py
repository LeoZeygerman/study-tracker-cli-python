def main_menu():
    while True:
        try:
            
            print('1.Добавить предмет')
            print('2.Посмотреть ваши предметы')
            print('3.Перейти в меню предметов')
            print('4.Выйти')
            choice = int(input('Ваш выбор: '))
            
            if choice == 1:
                pass
            
        except ValueError:
            print('Ошибка при вводе!')