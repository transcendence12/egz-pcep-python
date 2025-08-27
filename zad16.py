data = ((1, 2),) * 7
print(len(data[3:8]))

# To jest tuple jednoelementowa, która zawiera kolejny tuple (1, 2).

# Zwróć uwagę na przecinek: bez przecinka byłoby po prostu (1, 2) – tuple dwuelementowa.

# Ale ((1, 2),) to tuple z jednym elementem: (1, 2).

# 👉 Wynik:

# ((1, 2),)  →  [ (1, 2) ]

# 2. * 7

# Powtarzamy ten tuple 7 razy.

# 👉 Wynik:

# data = ((1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2))


# czyli tuple długości 7.

# 3. data[3:8]

# Slice od indeksu 3 (włącznie) do 8 (wyłącznie).

# data ma indeksy od 0 do 6.

# Więc data[3:8] = elementy o indeksach 3, 4, 5, 6.

# To są 4 elementy.





# W Pythonie przecinek, a nie nawiasy, definiuje tuple.
# Nawiasy są tylko "opakowaniem", ale to przecinek decyduje, czy mamy tuple.

# Przykłady:
# x = (1)      
# to NIE jest tuple → tylko liczba całkowita 1

# y = (1,)     
# to jest tuple jednoelementowa → (1,)

# z = (1, 2)   
# to jest tuple dwuelementowa → (1, 2)