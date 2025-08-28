data = {}
data[1] = 1
data['1'] = 2
data[1.0] = 4

res = 0

for d in data:
    res += data[d]

print(res)

# Opcje:
# 3
# The code is erroneous.
# 6
# 7


# 1️⃣ Dodawanie elementów do słownika

# data[1] = 1 → słownik: {1: 1}

# data['1'] = 2 → słownik: {1: 1, '1': 2} (klucz '1' jako string, różny od liczby)

# data[1.0] = 4

# Python traktuje int i float jako równe, jeśli mają tę samą wartość numeryczną jako klucze słownika

# 1 i 1.0 są tym samym kluczem w słowniku

# Dlatego zapis data[1.0] = 4 nadpisuje wcześniejszą wartość data[1] = 1

# Słownik po tym kroku:

# {1: 4, '1': 2}

# 2️⃣ Pętla for d in data

# Iterujemy po kluczach słownika: 1 i '1'

# Sumujemy wartości:

# res = 0
# res += data[1]   → res = 0 + 4 = 4
# res += data['1'] → res = 4 + 2 = 6

# 3️⃣ Wynik
# 6

# ✅ Prawidłowa odpowiedź:
# 6


# 💡 Podsumowanie:

# W słownikach Python int i float o tej samej wartości traktowane są jako ten sam klucz

# String '1' to już inny klucz

# To jest klasyczny "pułapka" przy mieszaniu typów numerycznych i stringów w słowniku