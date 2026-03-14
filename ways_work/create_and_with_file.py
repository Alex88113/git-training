from pathlib import Path
from datetime import datetime

def get_date_today(date=datetime.now()) -> str:
    formatted_date = date.strftime("%Y-%m-%d")
    return f"Date today: {formatted_date}"

def write_file() -> None:
    file = Path("hello.txt") # создание файла
    file.write_text(get_date_today()) # запись в файл
    content = file.read_text() # чтение текста

    if file.is_dir():
        print("is dir")
    else:
        print(f'not is dir\nname file: {file.name}')

write_file()



def check_file() -> bool:
    file = Path('first_program.py')
    if file.is_file():
        return True
    else:
        return False


print(check_file())
print('-' * 50)

file = Path(__file__)
print(f'Абсолютный путь до файла {file}')