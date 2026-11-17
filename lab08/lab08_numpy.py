import numpy as np

#1
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)
print("line:", line)
print("zeros:", zeros)
print("unknown_table:\n", unknown_table)
print("identity:\n", identity)

#2
print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2–5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("Массив в обратном порядке:", hours[::-1])

#3
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("Форма:", temperatures.shape)
print("Число измерений:", temperatures.ndim)
print("Число элементов:", temperatures.size)
print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])

center_fragment = temperatures[0:2, 1:3]
print("Центральный фрагмент 2x2:\n", center_fragment)
print("Форма центрального фрагмента:", center_fragment.shape)

#4
matrix = np.arange(1, 26).reshape(5, 5)

first_three_rows = matrix[:3]
print("Первые три строки:\n", first_three_rows)
print("shape:", first_three_rows.shape)

last_two_rows = matrix[-2:]
print("Последние две строки:\n", last_two_rows)
print("shape:", last_two_rows.shape)

first_two_cols = matrix[:, :2]
print("Первые два столбца:\n", first_two_cols)
print("shape:", first_two_cols.shape)

middle_slice = matrix[1:4, 2:5]
print("Строки 1–3 и столбцы 2–4:\n", middle_slice)
print("shape:", middle_slice.shape)

bottom_right = matrix[-2:, -2:]
print("Угловой блок 2x2 в правом нижнем углу:\n", bottom_right)
print("shape:", bottom_right.shape)