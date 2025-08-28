nums = [1, 2, 3]
vals = nums
del vals[:]


# 1️⃣ Przypisanie
# vals = nums


# Teraz obie zmienne wskazują na ten sam obiekt listy.

# nums i vals to referencje do tej samej listy.

# 2️⃣ del vals[:]

# vals[:] oznacza wszystkie elementy listy

# del vals[:] usuwa wszystkie elementy z listy, na którą wskazuje vals.

# Ponieważ nums i vals wskazują ten sam obiekt, lista nums również staje się pusta.

# 3️⃣ Stan po wykonaniu
# nums → []
# vals → []


# Długość obu list = 0

# Kod nie powoduje błędu

# ✅ Prawidłowa odpowiedź:
# nums and vals have the same length


# 💡 Wyjaśnienie:

# Przypisanie vals = nums → dwie zmienne wskazują tę samą listę

# del vals[:] usuwa wszystkie elementy listy, nie samą zmienną

# Dlatego długości obu list nadal są równe (oba 0)