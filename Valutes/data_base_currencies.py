import asyncio

import asyncpg

def get_data_connect():
    settings_connect = {
        "user": "postgres",
        "password": "postgres",
        "database": "currencies_valutes",
        "host": "localhost"
    }
    return settings_connect

async def initial_db() -> None:
    conn = await asyncpg.connect(get_data_connect())
    await conn.execute("""
    CREATE TABLE IF NOT EXISTS currencies (
    id SERIAL PRIMARY KEY,
    title_values TEXT NOT NULL,
    price INTEGER,
    
    """)

