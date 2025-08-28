my_list = [x * x for x in range(5)]

def fun(lst):
    del lst[lst[2]]
    return lst

print(fun(my_list))




# my_list = [x * x for x in range(5)]
# To jest list comprehension: x * x dla każdego x z range(5) → czyli z liczb od 0 do 4.

# Rozpisane:

# x=0 → 0*0 = 0

# x=1 → 1*1 = 1

# x=2 → 2*2 = 4

# x=3 → 3*3 = 9

# x=4 → 4*4 = 16

# ➡️ więc my_list = [0, 1, 4, 9, 16]

# 2️⃣ Definicja funkcji
# python
# Kopiuj
# Edytuj
# def fun(lst):
#     del lst[lst[2]]
#     return lst
# Funkcja przyjmuje listę lst.

# Wewnątrz: del lst[lst[2]]

# 👉 Trzeba uważać:

# lst[2] to element listy o indeksie 2.

# W naszej liście: lst = [0, 1, 4, 9, 16], więc lst[2] = 4.

# To oznacza, że kasujemy element o indeksie 4 (del lst[4]).

# 3️⃣ Usuwanie elementu
# Lista przed usunięciem:

# csharp
# Kopiuj
# Edytuj
# [0, 1, 4, 9, 16]
# del lst[4] usuwa element o indeksie 4 (ostatni, czyli 16).

# Lista po usunięciu:

# csharp
# Kopiuj
# Edytuj
# [0, 1, 4, 9]
# 4️⃣ Zwracanie listy
# Funkcja zwraca tę zmodyfikowaną listę.

# 5️⃣ Wynik
# python
# Kopiuj
# Edytuj
# print(fun(my_list))
# ➡️ output:

# csharp
# Kopiuj
# Edytuj
# [0, 1, 4, 9]
# ✅ Podsumowanie:

# Najpierw tworzymy [0,1,4,9,16]

# Potem bierzemy trzeci element (4), traktujemy go jako indeks

# Kasujemy element o indeksie 4 → czyli 16

# Zostaje [0,1,4,9]
