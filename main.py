from storage import save_data, load_data
from main_menu import main_menu
from study_menu import study_menu

data = load_data()

if len(data) == 0:
    current = 'main'
else:
    current = 'study'

while True:
    if current == 'main':
        current = main_menu()
    elif current == 'study':
        current = study_menu()