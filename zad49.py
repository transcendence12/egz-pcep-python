data = ['Peter', 'Paul', 'Mary']
print(data[int(-1/2)])

# 1️⃣ Obliczenie -1/2

# W Pythonie operator / zawsze daje wynik zmiennoprzecinkowy (float).

# -1 / 2 = -0.5

# 2️⃣ Funkcja int(-0.5)

# Funkcja int() ucina część ułamkową (zaokrągla w stronę zera).

# int(-0.5) == 0

# ⚠️ To ważne: int(-0.5) nie daje -1, tylko 0.
# (bo int() nie działa jak matematyczna podłoga floor(), tylko "obcina" do zera).

# 3️⃣ Indeksowanie listy

# Ostatecznie zostaje:

# print(data[0])


# A element pod indeksem 0 to 'Peter'.

# ✅ Output
# Peter

# int(x)

# obcina część ułamkową → tzw. "truncation towards zero".

# Czyli zawsze "przesuwa w stronę zera":

# int(2.9) == 2

# int(-2.9) == -2

# math.floor(x)

# zawsze zaokrągla w dół (w stronę -∞)

# math.floor(2.9) == 2

# math.floor(-2.9) == -3