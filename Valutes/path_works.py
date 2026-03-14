from pathlib import Path

current_file = Path(__file__).parent
parent_dir = current_file.parent
print(f"Текущее место положение {current_file}")
print(f"Поднялись на уровень выше {parent_dir}")


