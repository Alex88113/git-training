import pytest

from get_today import get_today_date

@pytest.mark.parametrize('expected', [
    ('2026-03-14'),
    ('2026-03-14'),
    ('2026-03-14')
])
def test_get_date(expected):
    assert get_today_date() == expected
