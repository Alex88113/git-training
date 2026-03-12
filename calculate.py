from typing import Dict

class Calculate:
    def __init__(self, number1: int | float, number2: int | float) -> None:
        if not all(isinstance(num, int | float) for num in (number1, number2)):
            raise ValueError("Одна или обе переменные содержать некорректный тип данных")
        if number1 < 0:
            raise ValueError('число в number1 не может быть отрицательным')
        if number2 < 0:
            raise ValueError('число в number2 не может быть отрицательным')

        self.number1 = number1
        self.number2 = number2

    def print_info(self) -> Dict[str, int | float]:
        return {
            "number1": self.number1,
            "number2": self.number2
        }

class Adding(Calculate):
    def __init__(self, number1, number2) -> None:
        super().__init__(number1, number2)

    def add_numbers(self) -> float:
        return self.number1 + self.number2

class Subtraction(Calculate):
    def __init__(self, number1, number2) -> None:
        super().__init__(number1, number2)

    def sub_numbers(self) -> float:
        return self.number1 - self.number2

class Multiply(Calculate):
    def __init__(self, number1, number2) -> None:
        super().__init__(number1, number2)

    def multi_numbers(self) -> int:
        return self.number1 * self.number2

class Division(Calculate):
    def __init__(self, number1, number2) -> None:
        super().__init__(number1, number2)

    def division_numbers(self) -> float:
        try:
            result = self.number1 / self.number2
        except ZeroDivisionError as error:
            raise ZeroDivisionError(f"Возникла ошибка при делении на 0: {error}")
        except TypeError as error:
            raise TypeError(f"Операция с неверным типом данных")

        return float(self.number1 // self.number2)

class StartCalculate:
    def __init__(self) -> None:
        try:
            self.add = Adding(232, -78)
            self.sub = Subtraction(100, 234)
            self.multi = Multiply(100, 34)
            self.div = Division(100, 34)
        except TypeError as error:
            raise TypeError(f'Ошибка с типами данных при создании объекта')

    def print_info_result(self) -> None:
        print(self.add.add_numbers())
