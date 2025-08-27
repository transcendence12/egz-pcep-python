# my_tuple[1] = my_tuple[1] + my_tuple[0] próbuje zmienić element o indeksie 1, co w przypadku krotki jest niedozwolone.
# TypeError: 'tuple' object does not support item assignment


# Trzeba stworzyć nową tuple, bo starej nie da się zmienić:

# my_tuple = (my_tuple[0], my_tuple[1] + my_tuple[0], my_tuple[2])
# print(my_tuple)  


# 👉 wynik:

# (10, 30, 30)

# LUB

# Bardziej ogólny sposób (jeśli tuple ma wiele elementów):

# Możesz przekonwertować tuple na listę (mutable), zmienić element i zrobić tuple z powrotem:

# my_tuple = (10, 20, 30)

# temp_list = list(my_tuple)  # zamiana na listę
# temp_list[1] = temp_list[1] + temp_list[0]  # zmiana
# my_tuple = tuple(temp_list)  # z powrotem na tuple

# print(my_tuple)


# 👉 wynik:

# (10, 30, 30)