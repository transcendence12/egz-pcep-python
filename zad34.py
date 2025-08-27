L = [i for i in range(-1, -2)]

# ile elementów zawiera powyższa lista? Odp: zero elementów


# 1️⃣ range(-1, -2)

# range(start, stop) generuje liczby od start do stop - 1, czyli nie obejmuje stop.

# Tutaj: start = -1, stop = -2

# Ponieważ start > stop i krok domyślny = 1, Python nie wygeneruje żadnej liczby.

# W skrócie: zakres jest pusty.

# 2️⃣ List comprehension [i for i in range(-1, -2)]

# Ponieważ range(-1, -2) jest pusty, lista też będzie pusta:

# L = []

# ✅ Ile elementów ma lista?

# len(L) = 0