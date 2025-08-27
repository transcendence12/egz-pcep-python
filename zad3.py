x = [0, 1, 2]          # początkowo lista = [0, 1, 2]

x.insert(0, 1)         # wstawiamy "1" na indeks 0
# teraz x = [1, 0, 1, 2]

del x[1]               # usuwamy element o indeksie 1 (czyli "0")
# teraz x = [1, 1, 2]

print(sum(x))          # suma = 1 + 1 + 2 = 4