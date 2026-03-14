from pathlib import Path


def get_info_about_ways():
    home_dir = Path.home()
    config = Path.home() / " .config" / "app" / "settings.ini"
    script_dir = Path(__file__).parent
    file = Path('first_program.py')


    print(f'Домашняя папка юзера {home_dir}')
    print(f'Скрипт находится в папке {script_dir}')
    print(f"Соединенный путь {config}")
    print(file.name)
    print(file.parent)


get_info_about_ways()

print('-' * 70)

def check_folder():
    folder = Path('.')
    list_file = []
    list_dir = []

    for item in folder.iterdir():
        print(item.name)

    for item in folder.iterdir():
        if item.is_file():
            list_file.append(item.name)

        elif item.is_dir():
            list_dir.append(item.name)

    print(f"Файлы {list_file}\nПапки {list_dir}")

check_folder()