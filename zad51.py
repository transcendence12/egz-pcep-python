data = {1:0, 2:1, 3:2, 0:1}
x=0

for _ in range(len(data)):
    x = data[x]

print(x)


# funkcję wbudowaną len() działa na słownikach.

# len(data) zwraca liczbę par klucz:wartość w słowniku.

# Przykład:

# data = {1:0, 2:1, 3:2, 0:1}
# print(len(data))  # 4, bo są 4 pary klucz:wartość

# 2️⃣ Analiza kodu
# data = {1:0, 2:1, 3:2, 0:1}
# x = 0

# for _ in range(len(data)):  # czyli 4 razy
#     x = data[x]


# Słownik data wygląda tak:

# klucz → wartość
# 1 → 0
# 2 → 1
# 3 → 2
# 0 → 1

# Iteracje pętli:

# Początek: x = 0

# Pierwsza iteracja:
# x = data[0] = 1

# Druga iteracja:
# x = data[1] = 0

# Trzecia iteracja:
# x = data[0] = 1

# Czwarta iteracja:
# x = data[1] = 0

# 3️⃣ Wynik

# Po zakończeniu pętli:

# print(x)   # 0