dct = {}
dct["1"] = (1,2)
dct["2"] = (2,1)

for x in dct.keys():
    print(dct[x][1], end='')  

# 21

# 1. Co mamy w słowniku?
# dct = {
#     "1": (1, 2),
#     "2": (2, 1)
# }


# klucz "1" → wartość (1,2)

# klucz "2" → wartość (2,1)

# 2. Iteracja for x in dct.keys()

# W Pythonie od wersji 3.7+ (a od 3.6 w CPython) słowniki zachowują kolejność dodawania kluczy.
# Czyli iteracja pójdzie najpierw po "1", potem po "2".

# 3. Co się dzieje w print(dct[x][1], end='')

# dct[x] zwraca krotkę przypisaną do danego klucza.

# [1] → to drugi element krotki (indeksowanie od 0).

# 👉 Iteracja:

# x = "1" → dct["1"] = (1,2) → dct["1"][1] = 2
# → wydrukuje 2

# x = "2" → dct["2"] = (2,1) → dct["2"][1] = 1
# → wydrukuje 1

# Wszystko wypisywane w jednym ciągu, bez spacji (end='').

# 21