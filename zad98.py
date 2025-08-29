x = 1
x = x == x


# The value eventually assigned to x is equal to:
# Opcje:
# 1
# 0
# True - PRAWIDŁOWA ODPOWIEDŹ
# False


# Krok 1: x = 1

# Teraz x przechowuje liczbę całkowitą 1.

# Krok 2: x = x == x

# Operator == porównuje dwie wartości i zwraca True lub False.

# Wyrażenie x == x to: 1 == 1 → True

# Następnie przypisujesz wynik porównania do x:

# x = True

# Kluczowa rzecz:

# == nie zwraca liczby 1 ani 0, tylko boola (True lub False).

# W Pythonie True zachowuje się jak 1 przy działaniach matematycznych, np.:

# x = True
# print(x + 1)  # wynik: 2


# ✅ Podsumowanie:
# Wynik to True, bo operator == zawsze zwraca wartość logiczną (bool), a nie liczbę.