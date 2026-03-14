import asyncio
from typing import Dict, Any

import httpx

class Currencies:
    def __init__(self) -> None:
        self.url: str = "https://www.cbr-xml-daily.ru/daily_json.js"
        self.client = httpx.AsyncClient(
            timeout=15.0,
            headers={"Accept": "application/json"}
        )

    async def closing_session(self) -> None:
        await self.client.aclose()

    async def get_request(self) -> Dict[str, Any]:
        try:
            resp = await self.client.get(self.url)
            data = resp.json()
            return data

        except httpx.TimeoutError as error:
            raise httpx.TimeoutError(f"Таймаут на подключение истёк: {error}")

        except httpx.ConnectError as error:
            raise httpx.ConnectError(f"Не удалось установить соединение с сервером")


    async def get_rate_euro(self) -> Dict[str, str | float]:
        data = await self.get_request()

        try:
            euro_rate = data["Valute"]["EUR"]
        except KeyError as error:
            raise KeyError(f"Ключа с таким именем нет")

        return {
            "Valute": euro_rate.get("Name"),
            "Quantity": euro_rate.get("Nominal"),
            "Price": euro_rate.get("Value")
        }

    async def get_rate_usd(self) -> Dict[str, str | float]:
        data = await self.get_request()

        try:
            dollars_rate = data["Valute"]["USD"]
        except KeyError as error:
            raise KeyError(f"Ключа с таким названием нет: {error}")

        return {
            "Valute": dollars_rate.get('Name'),
            "Quantity": dollars_rate.get("Nominal"),
            "Price": dollars_rate.get("Value")
        }
