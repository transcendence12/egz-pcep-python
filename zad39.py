fruits1 = ['Apple', 'Pear', 'Banana']
fruits2 = fruits1
fruits3 = fruits1[:]

fruits2[0] = 'Cherry' 
fruits3[1] = 'Orange'        

res = 0

for i in (fruits1, fruits2, fruits3):
    if i[0] == 'Cherry':
        res += 1
    if i[1] == 'Orange':
        res += 10
print(res)

# odpowiedz: res = 12



# fruits1 → ['Apple', 'Pear', 'Banana']

# fruits2 = fruits1
# 👉 fruits2 nie tworzy nowej listy, tylko wskazuje na ten sam obiekt w pamięci, co fruits1.

# fruits3 = fruits1[:]
# 👉 [:] tworzy płytką kopię listy → nowy obiekt, ale z tymi samymi wartościami.

# fruits2[0] = 'Cherry'
# Zmieniasz pierwszy element listy wskazywanej przez fruits2.

# Ale ponieważ fruits2 i fruits1 to ten sam obiekt → zmiana dotyczy obu.

# Teraz:

# fruits1 = ['Cherry', 'Pear', 'Banana']

# fruits2 = ['Cherry', 'Pear', 'Banana']

# fruits3 = ['Apple', 'Pear', 'Banana']

# fruits3[1] = 'Orange'
# Zmieniasz drugi element w fruits3 (to osobna kopia).

# Teraz:

# fruits1 = ['Cherry', 'Pear', 'Banana']

# fruits2 = ['Cherry', 'Pear', 'Banana']

# fruits3 = ['Apple', 'Orange', 'Banana']

# Iterujemy po 3 listach: fruits1, fruits2, fruits3.

# Dla fruits1 = ['Cherry', 'Pear', 'Banana']

# i[0] == 'Cherry' → ✅ → res = 1

# i[1] == 'Orange' → ❌

# Dla fruits2 = ['Cherry', 'Pear', 'Banana']

# i[0] == 'Cherry' → ✅ → res = 2

# i[1] == 'Orange' → ❌

# Dla fruits3 = ['Apple', 'Orange', 'Banana']

# i[0] == 'Cherry' → ❌

# i[1] == 'Orange' → ✅ → res = 12

# 4️⃣ Wynik
# print(res)  # 12