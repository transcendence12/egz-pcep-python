list1 = [1, 3]
list2 = list1
list1[0] = 4
print(list2)


# list1 = [1, 3]     # list1 → [1, 3]
# list2 = list1      # list2 wskazuje na TĘ SAMĄ listę co list1
# list1[0] = 4       # zmieniamy pierwszy element listy (z 1 na 4)
# print(list2)
# 👉 ponieważ list2 to referencja do tej samej listy, co list1, zmiana w list1 jest też widoczna w list2.

# Wynik:

# [4, 3]
# ⚡️ Jeśli chciałabyś, żeby list2 było kopią a nie referencją, trzeba zrobić np.:

# list2 = list1.copy()
# Wtedy list1[0] = 4 nie zmieni list2.