import math


assert list(filter(lambda x: x % 2 == 0, [2, 5, 1, 4, 3, 6, 7, 8, 9])) == [2, 4, 6, 8], 'Не коррктно работает функция'
assert list(map(lambda x: x**3, [2, 5, 1, 4, 3, 6, 7, 8, 9])) == [8, 125, 1, 64, 27, 216, 343, 512, 729], 'Не коррктно работает функция'
assert sorted([2, 5, 1, 4, 3, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert str(math.pi)[:4] == '3.14', 'Не корректное значение функции'
assert math.sqrt(9) == 3
assert math.pow(2, 4) == 16
assert math.hypot(5, 12) == 13
