l1 = [1,2,3]
for v in range(len(l1)):
    l1.insert(1, l1[v])

print(l1)

# opcje:
# [1, 2, 3, 1, 2, 3]
# [3, 2, 1, 1, 2, 3]
# [1, 1, 1, 1, 2, 3]
# [1, 2, 3, 3, 2, 1]



# 1️⃣ Inicjalizacja
# l1 = [1, 2, 3]

# 2️⃣ Pętla for v in range(len(l1))

# range(len(l1)) = range(3) → v = 0, 1, 2

# UWAGA: len(l1) jest obliczone przed rozpoczęciem pętli, więc iteracja przebiega tylko 3 razy, mimo że lista rośnie.

# 3️⃣ Krok po kroku:
# Iteracja 0 (v = 0):
# l1.insert(1, l1[0])  # wstawiamy l1[0] = 1 na indeks 1

# l1 = [1, 1, 2, 3]

# Iteracja 1 (v = 1):
# l1.insert(1, l1[1])  # l1[1] = 1

# l1 = [1, 1, 1, 2, 3]

# Iteracja 2 (v = 2):
# l1.insert(1, l1[2])  # l1[2] = 1

# l1 = [1, 1, 1, 1, 2, 3]

# 4️⃣ Wynik
# [1, 1, 1, 1, 2, 3]

# ✅ Prawidłowa odpowiedź:
# [1, 1, 1, 1, 2, 3]


# 💡 Wyjaśnienie:

# insert(1, value) wstawia element na indeks 1 przesuwając pozostałe elementy w prawo.

# Wartość l1[v] odczytywana jest w trakcie iteracji, więc zmiany w liście wpływają na kolejne odczyty.

# Długość listy nie zmienia liczby iteracji, bo range(len(l1)) była ustalona na początku.








