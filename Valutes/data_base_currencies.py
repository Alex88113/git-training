import asyncio

import asyncpg
from loguru import logger

settings_connect = {
    "user": "postgres",
    "password": "postgres",
    "database": "currencies_valutes",
    "host": "localhost"
}

async def initial_db() -> None:
    logger.debug("Инициализация бд...")
    conn = await asyncpg.connect(**settings_connect)
    await conn.execute("""
    CREATE TABLE IF NOT EXISTS currencies (
    id SERIAL PRIMARY KEY,
    title_valute TEXT NOT NULL,
    quantity_valute INTEGER,
    price FLOAT
    )
    """)
    await conn.close()
    logger.debug("БД СОЗДАНА!")


async def insert_data(valute: str, price: float, quantity_valute: int) -> None:
    conn = await asyncpg.connect(**settings_connect)

    logger.debug("Начало проверки типов параметров")
    if not isinstance(valute, str):
        raise ValueError("Требуется строковое название валюты")
    logger.info("получено название валюты: {t}", t=valute)

    if not isinstance(price, float) or price < 0:
        raise ValueError("цена валюты отрицательна либо не является вещественным числом")
    logger.info("получена цена валюты: {p}", p=price)

    if not isinstance(quantity_valute, int) or quantity_valute < 0:
        raise ValueError("Кол во валюты необходимо указать в целом числе или не должно быть отрицательным")
    logger.info("получено кол во валюты: {q}", q=quantity_valute)

    logger.debug("Проверка завершена")

    logger.debug("Вставка данных в таблицу")
    await conn.execute('''
    INSERT INTO currencies (title_valute, price, quantity_valute)
    VALUES ($1, $2, $3) ''', valute, price, quantity_valute)

    await conn.close()
    logger.debug("Вставка завершена")
