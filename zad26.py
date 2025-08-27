# list.reverse() ✅

# To metoda listy, która odwraca listę w miejscu (in-place).

# Nie tworzy nowej listy, tylko modyfikuje istniejącą:

# my_list = [1, 2, 3, 4]
# my_list.reverse()
# print(my_list)  # [4, 3, 2, 1]


# reversed(list) ✅

# reversed() to wbudowana funkcja, która zwraca iterator odwróconej listy, nie modyfikuje listy oryginalnej.

# Jeśli chcesz listę, trzeba ją przekonwertować:

# my_list = [1, 2, 3, 4]
# rev_list = list(reversed(my_list))
# print(rev_list)  # [4, 3, 2, 1]
# print(my_list)   # [1, 2, 3, 4]  (oryginał nie zmieniony)