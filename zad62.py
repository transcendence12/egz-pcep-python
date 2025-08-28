data = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

for i in range(0, 4):  
    print(data[i].pop(), end=' ')


# 1️⃣ Struktura danych

# data to lista list (czyli faktycznie lista zagnieżdżona).
# Każdy element data[i] to osobna lista:

# data[0] = [1, 2, 3, 4]

# data[1] = [5, 6, 7, 8]

# data[2] = [9, 10, 11, 12]

# data[3] = [13, 14, 15, 16]

# 2️⃣ Metoda .pop()

# list.pop() bez argumentu usuwa ostatni element listy i go zwraca.
# Czyli:

# data[0].pop() → usuwa 4 z [1, 2, 3, 4] i zwraca 4.

# data[1].pop() → usuwa 8 z [5, 6, 7, 8] i zwraca 8.

# data[2].pop() → usuwa 12 z [9, 10, 11, 12] i zwraca 12.

# data[3].pop() → usuwa 16 z [13, 14, 15, 16] i zwraca 16.

# 3️⃣ Pętla

# for i in range(0, 4): → i = 0, 1, 2, 3
# Dla każdego i wywołujemy .pop() na data[i].

# 4️⃣ Wynik

# Kolejno wypisze:

# 4 8 12 16

# 5️⃣ Stan listy po pętli

# Po usunięciu ostatnich elementów, data wygląda tak:

# [
#     [1, 2, 3],
#     [5, 6, 7],
#     [9, 10, 11],
#     [13, 14, 15]
# ]


# ✅ Podsumowanie:
# Tak, data to lista zagnieżdżona (lista list).
# Kod działa tak, że z każdej wewnętrznej listy usuwa i wypisuje ostatni element.
