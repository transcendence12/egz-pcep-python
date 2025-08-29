# What is the expected output of the following code?

x = 1 / 2 + 3 // 3 + 4 ** 2

print(x)


# Opcje:
# 17
# 17.5 - PRAWIDŁOWA ODPOWIEDŹ
# 8.5
# 8


# 1. Kolejność operatorów w Pythonie

# Priorytety są takie (od najwyższego w tej linijce):

# ** → potęgowanie

# / i // → dzielenie i dzielenie całkowite (ten sam poziom)

# + → dodawanie

# 2. Obliczenia krok po kroku

# ➡️ Najpierw potęgowanie:

# 4 ** 2 = 16


# ➡️ Teraz dzielenia (/ i //):

# 1 / 2 = 0.5 (dzielenie zwykłe, zawsze float)

# 3 // 3 = 1 (dzielenie całkowite → wynik int)

# ➡️ Teraz mamy:

# x = 0.5 + 1 + 16


# ➡️ Dodawanie:

# x = 17.5

# ✅ Wynik:
# print(x)  # 17.5

