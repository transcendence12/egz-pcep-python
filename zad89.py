# What is the expected output of the following code?

x = 28

y = 8

print(x / y)


print(x // y)

print(x % y)



# opcje:

# 1 | 3.0 2 | 3 3 | 2
# 1 | 3.5 2 | 3 3 | 4
# 1 | 3 2 | 3.5 3 | 4
# 1 | 3.5 2 | 3.5 3 | 2


# 1️⃣ x / y → dzielenie zwykłe (/)
# 28 / 8 = 3.5


# Zawsze zwraca float, nawet jeśli dzielenie jest całkowite.

# 2️⃣ x // y → dzielenie całkowite (//)
# 28 // 8 = 3


# Wynik to liczba całkowita, bo // zaokrągla w dół.

# 3️⃣ x % y → reszta z dzielenia (%)
# 28 % 8 = 4


# Bo 8 * 3 = 24, a 28 - 24 = 4

# ✅ Wynik wydruku:
# 3.5
# 3
# 4

# ✅ Prawidłowa opcja z listy:
# 1 | 3.5 2 | 3 3 | 4