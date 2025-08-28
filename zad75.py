data = {'z': 23, 'x':7, 'y':42}

for _ in sorted(data):
    print(data[_], end=' ')

# 1️⃣ Słownik data
# data = {'z': 23, 'x': 7, 'y': 42}


# Klucze: 'z', 'x', 'y'

# Wartości: 23, 7, 42

# 2️⃣ Funkcja sorted(data)

# sorted(data) sortuje klucze słownika w kolejności alfabetycznej.

# Klucze: 'x', 'y', 'z'

# 3️⃣ Pętla for _ in sorted(data)

# Iterujemy po posortowanych kluczach:

# _ = 'x', 'y', 'z'

# 4️⃣ Dostęp do wartości
# print(data[_], end=' ')


# data['x'] → 7

# data['y'] → 42

# data['z'] → 23

# 5️⃣ Wynik
# 7 42 23


# ✅ Podsumowanie:

# sorted(data) sortuje klucze słownika.

# W pętli _ to po prostu zmienna iterująca po tych kluczach.

# data[_] zwraca wartość przypisaną do danego klucza.