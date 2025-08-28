data = [[0,1,2,3] for i in range(2)]
print(data[2][0])


# 1️⃣ Co tworzy list comprehension?

# [ [0,1,2,3] for i in range(2) ]

# range(2) → generuje 0, 1 → czyli 2 elementy.

# Wynik:

# data = [
#     [0,1,2,3],   # dla i=0
#     [0,1,2,3]    # dla i=1
# ]

# 2️⃣ Co dalej?

# Masz tylko 2 elementy (data[0] i data[1]).

# Ale w kodzie odwołujesz się do:

# data[2][0]


# data[2] → próba dostępu do trzeciego elementu (indeks 2)

# Ale taki element nie istnieje, bo lista data ma tylko długość 2.

# 3️⃣ Błąd w Pythonie

# Dlatego Python wyrzuci:

# IndexError: list index out of range


# ✅ Podsumowanie:
# Błąd polega na tym, że próbujesz dostać się do data[2], mimo że lista data ma tylko indeksy 0 i 1.