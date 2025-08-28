data1 = 'a', 'b'
data2 = ('a', 'b')
print(data1 == data2)

# 1️⃣ Tworzenie krotek

# data1 = 'a', 'b' → w Pythonie przecinek sam w sobie tworzy krotkę, nawet jeśli nie użyto nawiasów.

# Czyli data1 to krotka ('a', 'b')

# data2 = ('a', 'b') → oczywiście też krotka ('a', 'b')

# 2️⃣ Porównanie
# data1 == data2


# Obie zmienne to krotki o tej samej długości i takich samych elementach w tej samej kolejności.

# Python porównuje krotki element po elemencie → są równe

# ✅ Wynik:
# True


# 💡 Wniosek:

# Nawiasy w krotce są opcjonalne, jeśli używasz przecinka.

# 'a', 'b' i ('a', 'b') to to samo w Pythonie.