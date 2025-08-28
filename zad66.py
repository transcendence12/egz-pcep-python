data = [1,2,3,4,5,6]

for i in range(1, 6):
    data[i-1] = data[i]

for i in range(0, 6):
    print(data[i], end=' ')


# Krok 1 – inicjalizacja
# data = [1, 2, 3, 4, 5, 6]

# Krok 2 – pętla for i in range(1,6)

# range(1,6) → wartości i = 1, 2, 3, 4, 5

# Każdy krok: data[i-1] = data[i] (czyli przesuwamy element w lewo).

# i = 1
# data[0] = data[1]
# [2, 2, 3, 4, 5, 6]

# i = 2
# data[1] = data[2]
# [2, 3, 3, 4, 5, 6]

# i = 3
# data[2] = data[3]
# [2, 3, 4, 4, 5, 6]

# i = 4
# data[3] = data[4]
# [2, 3, 4, 5, 5, 6]

# i = 5
# data[4] = data[5]
# [2, 3, 4, 5, 6, 6]

# Krok 3 – Drukowanie
# for i in range(0, 6):
#     print(data[i], end=' ')


# Lista końcowa:

# [2, 3, 4, 5, 6, 6]


# Wyjście:

# 2 3 4 5 6 6

# 🔎 Dlaczego tak się dzieje?

# Ten kod przesuwa całą listę w lewo.

# Każdy element na pozycji i-1 dostaje wartość z pozycji i.

# Ostatni element nie ma już czego dostać → zostaje nadpisany kopią poprzedniego.