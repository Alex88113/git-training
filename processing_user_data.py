from typing import Dict


class User:
    def __init__(self, name: str, age: int, email: str, password: str) -> None:
        if not isinstance(name, str):
            raise ValueError("Необходимо имя строкового формата")
        if not isinstance(password, str):
            raise ValueError("пароль не является строковым типом")
        if not isinstance(email, str):
            raise ValueError("email должен быть строкой")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Возраст не может быть отрицательным либо равным 0")

        self.name = name
        self.age = age
        self.email = email
        self.password = password


    def print_data_user(self) -> Dict[str, str | int]:
        return {
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'age': self.age
        }

    def processing_name(self) -> str:
        process_name = self.name.strip().lower().capitalize()
        return process_name

    def processing_email(self) -> str:
        process_email = self.email.strip().lower()
        return process_email

    def print_password(self) -> int:
        return len(self.password)

