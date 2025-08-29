
x = 9
y = 12

result = x // 2 * 2 / 2 + y % 2 ** 3
print(result)

# Opcje:
# 8
# 7.0
# 8.0 - PRAWIDŁOWA ODPOWIEDŹ
# 9.0


# Krok 1: Priorytety operatorów

# ** (potęgowanie) ma najwyższy priorytet

# potem %, //, *, / (od lewej do prawej)

# na końcu +

# Krok 2: Obliczamy y % 2 ** 3

# 2 ** 3 = 8

# y % 8 = 12 % 8 = 4

# Krok 3: Obliczamy x // 2 * 2 / 2

# x // 2 = 9 // 2 = 4 (dzielenie całkowite)

# 4 * 2 = 8

# 8 / 2 = 4.0 (dzielenie / zawsze daje float)

# Krok 4: Dodajemy wyniki

# 4.0 + 4 = 8.0

# ✅ Odpowiedź:

# 8.0







