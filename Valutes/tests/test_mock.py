import asyncio
import json

import pytest
import httpx
import respx
from httpx import Response

@pytest.mark.asyncio
async def test_basic_mock():
    with respx.mock:
        respx.get("https://api.example.com/rate").mock(
            return_value=Response(200, json={"rate": 92.5}) # создаёт сам http ответ
        )

        async with httpx.AsyncClient() as client:
            response = await client.get("https://api.example.com/rate")
            assert response.status_code == 200
            assert response.json()['rate'] == 92.5

            assert respx.calls.call_count == 1 # проверка перехвата запроса


@pytest.mark.asyncio
async def test_multiple_endpoints():
    router = respx.mock # можно создавать мок так, но потребуется активация
    router.get("https://api.example.com/usd").mock(
        return_value=Response(200, json={"rate": 92.5})
    )
    router.get("https://telegram.org").mock(
        return_value=Response(200)
    )

    router.get("https://example.com/eur").mock(
        return_value=Response(200, json={"rate": 99.8})
    )

    with router:
        async with httpx.AsyncClient() as client:
            resp = await client.get("https://telegram.org")
            assert resp.status_code == 200
            assert resp.status_code == 402


"""
Мокирование post запросов
"""
@respx.mock
@pytest.mark.asyncio
async def test_post_request():
    respx.post("https://api.example.com/rates").mock(
        return_value=Response(201, json={'status': 'created'})
    )

    async with httpx.AsyncClient() as client:
        resp = await client.post(
            'https://api.example.com/rates',
            json={"currency": "USD", "rate": 92.5}
        )

        assert resp.status_code == 201
        assert resp.json()['status'] == 'created'

        request = respx.calls.last.request
        assert request.method == 'POST'
        assert request.url == "https://api.example.com/rates"

        sent_data = json.loads(request.content)
        assert sent_data['currency'] == 'USD'
        assert sent_data['rate'] == 92.5

@respx.mock
@pytest.mark.asyncio
async def test_auth():
    respx.post("https://msapi.top-academy.ru/api/v2/auth/login").mock(
        return_value=Response(200, json={'access_token': "test-token", "refresh_token": "test-refresh-token"})
    )
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            "https://msapi.top-academy.ru/api/v2/auth/login",
            json={"username": "Kuche_mu73", "password": "6C3f6G3p"}
        )
        assert resp.status_code == 200
        assert resp.json()['access_token'] == "test-token"
        assert resp.json() is not None
