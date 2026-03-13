import os
import sys
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculate import (
Calculate,
Adding,
Subtraction,
Multiply,
Division
)

class TestAdd:
    @pytest.mark.parametrize("num1, num2, expected_result", [
        (10, 200, 210),
        (23, 54, 77),
        (10, 34, 44)
    ])

    def test_add(self, num1, num2, expected_result):
        obj_add = Adding(num1, num2)
        assert obj_add.add_numbers() == expected_result

class TestSub:
    @pytest.mark.parametrize("n1, n2, expected_result", [
        (190, 54, 136),
        (100, 34, 66),
        (1200, 88, 1112),
        (904, 34, 870)
    ])

    def test_sub(self, n1, n2, expected_result):
        sub = Subtraction(n1, n2)
        assert sub.sub_numbers() == expected_result

class TestMulti:
    @pytest.mark.parametrize("number1, number2, expected_result", [
        (2, 6, 12),
        (9, 9, 81),
        (15, 15, 225),
        (63, 23, 1449)
    ])

    def test_multi(self, number1, number2, expected_result):
        multi = Multiply(number1, number2)
        assert multi.multi_numbers() == expected_result

class TestDivision:
    @pytest.mark.parametrize("num1, num2, expected", [
        (10, 2, 5.0),
        (20, 5, 4.0),
        (100, 2, 50.0)
    ])
    
    def test_division(self, num1, num2, expected):
        div = Division(num1, num2)
        assert div.division_numbers() == expected
