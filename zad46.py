my_list_1 = [1, 2, 3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0, v)
print(my_list_2)

# Iteracja po my_list_1:

# Pierwszy element v = 1
# → my_list_2.insert(0, 1)
# → my_list_2 = [1]

# Drugi element v = 2
# → my_list_2.insert(0, 2)
# → my_list_2 = [2, 1]

# Trzeci element v = 3
# → my_list_2.insert(0, 3)
# → my_list_2 = [3, 2, 1]

# Wynik:
# [3, 2, 1]

# Dlaczego?

# 🔹 list.insert(index, value) wstawia element w określone miejsce.
# Tutaj zawsze wstawiasz na pozycję 0 → czyli na początek listy.

# Efekt: każdy kolejny element z my_list_1 ląduje na początku my_list_2, więc lista jest odwrócona.

# 👉 Czyli ten kod robi manualne odwracanie listy – taki własny sposób na reverse().