my_list =['Mary', 'had', 'a', 'little', 'lamb']

def my_list(my_list):
    del my_list[3]
    my_list[3] = 'ram'

print(my_list(my_list))

# Najpierw definiujesz zmienną globalną my_list (listę).

# Potem definiujesz funkcję o tej samej nazwie my_list.

# Funkcja nadpisuje referencję do listy.
# 👉 To oznacza, że od tego miejsca my_list oznacza funkcję, a nie listę.

# Dlatego w tym miejscu:

# print(my_list(my_list))


# Python próbuje wywołać funkcję my_list i przekazać jej samą siebie jako argument.
# Czyli my_list (funkcja) dostaje w parametrze my_list (też funkcję).

# 2️⃣ Próba użycia del my_list[3] na funkcji

# W ciele funkcji:

# del my_list[3]


# Oczekujesz, że my_list to lista, ale w rzeczywistości jest to funkcja (bo nazwy się zderzyły).
# Nie można indeksować ani usuwać elementów z funkcji → Python wywali błąd typu:

# TypeError: 'function' object is not subscriptable