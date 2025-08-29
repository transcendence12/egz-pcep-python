# What value will be assigned to the x variable?

z = 3
y = 7

x = y < z and z > y or y > z and z < y

# opcje:
# 0
# True - To jest prawidłowa odpowiedź
# False
# 1


# 1. Kolejność operatorów w Pythonie

# Najpierw porównania (<, >, <=, >=, ==, !=)

# Potem and

# Potem or

# 2. Podstawiamy wartości

# z = 3, y = 7

# Sprawdźmy każdy fragment:

# y < z → 7 < 3 → False

# z > y → 3 > 7 → False

# y > z → 7 > 3 → True

# z < y → 3 < 7 → True

# 3. Rozbijamy wyrażenie

# Mamy:

# x = (y < z and z > y) or (y > z and z < y)


# Podstawiamy:

# x = (False and False) or (True and True)


# (False and False) → False

# (True and True) → True

# Więc:

# x = False or True
# x = True

# ✅ Odpowiedź:

# Wartość zmiennej x to True ✔ bo W logice:

# False or True = True