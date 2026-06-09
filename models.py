from datetime import date, datetime

class Subject:
    def __init__(self, name, day_time, target, last_completed, complete):
        self.complete = complete
        self.name = name
        self.day_time = day_time
        self.target = target
        self.last_completed = last_completed
        
    def get_info(self):
        print(f'Предмет: {self.name} | Время в день: {self.day_time}\nЦель: {self.target}')
        
    def completed(self):
        today = date.today()
        if self.last_completed is None:
            self.last_completed = str(date.today())
            self.complete = 'Не отмечен'
            return
        last_date = datetime.strptime(self.last_completed, '%Y-%m-%d').date()
        difference = (today - last_date).days
        if difference >= 1:
            self.complete = 'Не отмечен'
        else:
            self.complete = 'Отмечен'
            
    def add_completed(self):
        if self.complete == 'Не отмечен':
            self.complete = 'Отмечен'
            print(f'Предмет {self.complete}')
        else:
            print(f'Предмет {self.complete}!')