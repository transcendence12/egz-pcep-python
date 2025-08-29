#  What is the expected output of the following code?

x = 1 + 1 // 2 + 1 / 2 + 2

print(x)

# 3
# 4.0
# 4
# 3.5 - PRAWIDŁOWA ODPOWIEDŹ


# Krok 1: Priorytety operatorów

# // i / mają wyższy priorytet niż +

# W obrębie // i / działa kolejność od lewej do prawej

# Krok 2: Obliczamy 1 // 2 i 1 / 2

# 1 // 2 → dzielenie całkowite → 0

# 1 / 2 → dzielenie float → 0.5

# Krok 3: Sumujemy wszystko
# 1 + 0 + 0.5 + 2


# 1 + 0 = 1

# 1 + 0.5 = 1.5

# 1.5 + 2 = 3.5

# ✅ Odpowiedź:

# 3.5




