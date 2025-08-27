nums = [1,2,3]
data = ('Peter', ) * len((nums)-nums[::-1][0])
print(data)


# 2️⃣ nums[::-1]

# [::-1] odwraca listę: [3, 2, 1].

# 3️⃣ nums[::-1][0]

# Pobieramy pierwszy element odwróconej listy: 3.

# 4️⃣ (nums) - nums[::-1][0] ❌

# Teraz próbujesz zrobić nums - 3.

# Problem: Python nie pozwala odejmować liczby od listy.

# To spowoduje błąd typu (TypeError):

# TypeError: unsupported operand type(s) for -: 'list' and 'int'

# 5️⃣ ('Peter', ) * len(...)

# Nawet gdyby odejmowanie działało, ('Peter',) * n tworzyłoby krotkę z n powtórzeniami 'Peter'.

# Ale w obecnej formie kodu nie zadziała, bo odejmowanie listy od liczby jest błędem.

# ✅ Wniosek

# Kod jest błędny i zwróci TypeError.