my_list = [1,2]
for v in range(2):
    my_list.insert(-1, my_list[v])

print(my_list)

# [1, 1, 1, 2]

# W Pythonie:

# Indeksy ujemne liczymy od końca:

# -1 → ostatni element

# -2 → przedostatni element

# -3 → trzeci od końca itd.

# Ale metoda insert(index, value) działa trochę inaczej:

# insert(i, x) wstawia element przed indeksem i.

# Jeśli dasz insert(-1, x), Python interpretuje to tak: “wstaw przed elementem o indeksie -1 (ostatnim elementem)”.

# Dlatego element trafia przed ostatnim elementem, a nie na jego miejsce.