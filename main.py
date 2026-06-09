from storage import save_data, load_data
from main_menu import main_menu
from study_menu import study_menu

data = load_data()

if len(data) == 0:
    main_menu()
else:
    study_menu()