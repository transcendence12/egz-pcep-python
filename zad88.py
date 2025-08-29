a = 1
b = 0
x = a or b
y = not(a and b)
print(x + y)





# Opcje:
# The output cannot be predicted.
# 2  - PRAWIDŁOWA ODPOWIEDŹ
# The program will cause an error.
# 1


# 1. Oblicz x = a or b

# a = 1, b = 0

# operator or zwraca pierwszą wartość „truthy”:

# 1 or 0 → 1

# więc:
# x = 1

# 2. Oblicz y = not(a and b)

# a and b → 1 and 0 → 0 (bo and zwraca pierwszą wartość falsy)

# not(0) → True

# w Pythonie True to 1

# więc:
# y = 1

# 3. Oblicz x + y

# x = 1, y = 1

# 1 + 1 = 2

# ✅ Wynik:

# 2