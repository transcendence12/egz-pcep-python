w = [7, 3, 23, 42]
x = w[1:]    [3, 23, 42]
y = w[1:]    [3, 23, 42]
z=w          [7, 3, 23, 42]
y[0] = 10    [10, 23, 42]
z[1] = 20    [7, 20, 23, 42]
print(w)

# [7, 20, 23, 42]


# 🔑 Wnioski

# Slicing w[1:] → tworzy nową listę (kopię fragmentu), zmiany w niej nie wpływają na oryginał.

# Przypisanie z = w → referencja do tego samego obiektu, zmiany wpływają na oba.
