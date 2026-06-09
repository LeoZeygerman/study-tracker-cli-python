class Subject:
    def __init__(self, name, day_time, target):
        self.name = name
        self.day_time = day_time
        self.target = target
        
    def get_info(self):
        print(f'Предмет: {self.name}\nВремя в день: {self.day_time}\nЦель: {self.target}')
        