import asyncio

from exchange_rate import *
from data_base_currencies import *

async def main():
    currencies = Currencies()
    await initial_db()

    data_get = await currencies.get_request()
    euro = await currencies.get_rate_euro()
    usd = await currencies.get_rate_usd()

    list_valute = [euro, usd]

    for i in list_valute:
        """
        Передаем полученные данные из словарей по определенным ключам
        """
        await insert_data(i['Valute'], i['Price'], i['Quantity'])

    await currencies.closing_session() # закрытие соединения

asyncio.run(main())
