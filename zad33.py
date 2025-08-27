data = {'a':1, 'b':2, 'c':3}
print(data['a', 'b'])

# Co próbujesz zrobić?

# Wygląda, jakbyś chciała pobrać dwa elementy słownika naraz ('a' i 'b').

# W Pythonie słownik akceptuje tylko pojedynczy klucz w nawiasach [].

# Jeśli napiszesz data['a', 'b'], Python traktuje to jako pojedynczy klucz, którym jest krotka ('a', 'b').

# 2️⃣ Sprawdzenie klucza w słowniku

# Twój słownik ma klucze 'a', 'b', 'c'

# Nie ma klucza ('a', 'b') (krotki)

# 3️⃣ Co się stanie?

# Python zgłosi błąd KeyError:

# KeyError: ('a', 'b')