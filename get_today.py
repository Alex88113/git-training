from datetime import datetime
from typing import Callable

def get_today_date() -> str:
    date = datetime.now()
    formatted_date = date.strftime("%Y-%m-%d")
    return formatted_date


def valid_date(date: Callable) -> bool:
    if type(date) is str:
        return True
    else:
        return False

def main():
    today = get_today_date()
    result = valid_date(today)
    print(result)

main()