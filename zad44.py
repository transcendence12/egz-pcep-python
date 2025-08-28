data = ['abc', 'def', 'abcde', 'efg']
print(max(data))


# Jak działa max() na stringach?

# W Pythonie max() porównuje elementy listy.

# Jeśli elementy są stringami → porównanie odbywa się leksykograficznie (tak jak w słowniku, ale według kodów ASCII/Unicode).

# Porównywane są litery od lewej do prawej.

# "abc" vs "def" → 'd' > 'a' → wygrywa "def".

# "def" vs "abcde" → 'd' > 'a' → nadal "def".

# "def" vs "efg" → 'e' > 'd' → wygrywa "efg".

# ✅ Wynik
# efg
