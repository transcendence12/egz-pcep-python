# after execution of the following snippet, the sum of all vals elements will be equal to: 4,5,2,3?
vals = [0, 1, 2]
vals.insert(0, 1)
del vals[1]

vals.insert(0, 1)

# insert(index, value) wstawia wartość przed podanym indeksem.

# vals.insert(0, 1) → wstawiamy 1 na początek listy:

# [1, 0, 1, 2]

# del vals[1]

# del vals[index] usuwa element o podanym indeksie.

# del vals[1] → usuwa element o indeksie 1, czyli 0:

# [1, 1, 2]

# Suma elementów
# 1 + 1 + 2 = 4

# ✅ Odpowiedź

# Po wykonaniu kodu suma elementów listy vals wynosi 4