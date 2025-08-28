box ={}
jars = {}
crates = {}

box['biscuit'] = 1
box['cake'] = 3

jars['jam'] = 4

crates['box'] = box
crates['jars'] = jars

print(len(crates['box']))

# 1️⃣ Tworzymy słowniki

# box = {} → pusty słownik

# jars = {} → pusty słownik

# crates = {} → pusty słownik

# 2️⃣ Dodajemy elementy
# box['biscuit'] = 1
# box['cake'] = 3


# box teraz: {'biscuit': 1, 'cake': 3}

# jars['jam'] = 4


# jars teraz: {'jam': 4}

# 3️⃣ Tworzymy "słownik słowników"
# crates['box'] = box
# crates['jars'] = jars


# crates teraz wygląda tak:

# {
#     'box': {'biscuit': 1, 'cake': 3},
#     'jars': {'jam': 4}
# }

# 4️⃣ len(crates['box'])

# crates['box'] → zwraca słownik {'biscuit': 1, 'cake': 3}

# len() słownika liczy liczbę kluczy, nie wartości

# {'biscuit', 'cake'} → 2 klucze

# ✅ Wynik:
# 2
