data = (1,2,3,4)
data = data[-2:-1]
data = data[-1]
print(data)

# ➡️ Slicing ([-2:-1]) oznacza:

# zacznij od elementu na pozycji -2 (czyli trzeciego od końca → 3)

# idź do elementu przed indeksem -1 (czyli przed ostatnim → przed 4)

# W efekcie dostajemy krotkę:

# data = (3,)


# ⚠️ Zwróć uwagę: to wciąż jest krotka jednoelementowa, a nie sama liczba 3.

# data = data[-1]


# ➡️ Teraz z tej krotki (3,) pobierasz element o indeksie -1 (czyli ostatni).
# Dostajesz:

# data = 3

# print(data)


# ➡️ Wynik:

# 3

# 🔑 Podsumowanie

# Po pierwszym slicingu masz krotkę jednoelementową (3,).

# Po drugim kroku wyciągasz z niej wartość 3.