data = {}
data['2'] = [1,2]
data['1'] = [3,4]

for i in data.keys():
    print(data[i][1], end='')


#     1️⃣ Tworzymy pusty słownik
# data = {}


# Na początku data jest pusty: {}.

# 2️⃣ Dodajemy elementy
# data['2'] = [1,2]
# data['1'] = [3,4]


# Teraz słownik wygląda tak:

# {
#   '2': [1, 2],
#   '1': [3, 4]
# }


# klucz '2' → wartość [1,2]

# klucz '1' → wartość [3,4]

# 3️⃣ Iteracja po keys()
# for i in data.keys():
#     print(data[i][1], end='')


# data.keys() → zbiór kluczy: ['2', '1']
# ⚠️ Uwaga: w Pythonie od wersji 3.7 słowniki pamiętają kolejność dodawania kluczy.
# Więc pętla pójdzie w kolejności '2' → '1'.

# 4️⃣ Iteracje w pętli

# Iteracja 1:
# i = '2'
# data['2'] = [1,2]
# data['2'][1] = 2
# → wydrukuje 2

# Iteracja 2:
# i = '1'
# data['1'] = [3,4]
# data['1'][1] = 4
# → wydrukuje 4

# 5️⃣ Wynik końcowy

# Na ekranie zobaczymy:

# 24


# (end='' sprawia, że liczby drukują się obok siebie, bez spacji i nowej linii).

# ✅ Podsumowanie: Kod wypisze 24, bo w każdej liście bierzemy element o indeksie 1 (drugi element) i drukujemy je w kolejności dodania kluczy.