import asyncio
import pytest
import pytest_asyncio

async def fetch_data():
    await asyncio.sleep(0.1)
    return {"data": 42}

@pytest.mark.asyncio
async def test_fetch_data():
    result = await fetch_data()
    assert result['data'] == 42