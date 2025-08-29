# Which of the following statements are true? (Choose two.)

# The result of the / operator is always an integer value.
# The ** operator uses right-sided binding. - PRAWIDŁOWA ODPOWIEDŹ
# The right argument of the % operator cannot be zero. - PRAWIDŁOWA ODPOWIEDŹ
# Addition precedes multiplication. - FAŁSZ


# Wyjasnienie:
# The result of the / operator is always an integer value.
# W Pythonie a / b zawsze zwraca liczbę zmiennoprzecinkową (float), nawet jeśli dzielisz liczby całkowite.

# Przykład:

# 4 / 2  # wynik: 2.0, czyli float
# 5 / 2  # wynik: 2.5


# ✅ Fałsz. Nie zawsze jest integer.

# The ** operator uses right-sided binding.

# Operator ** (potęgowanie) w Pythonie jest prawo-łączny, czyli jest stosowany od prawej do lewej.

# Przykład:

# 2 ** 3 ** 2
# # Jest interpretowane jako 2 ** (3 ** 2), a nie (2 ** 3) ** 2
# # Wynik: 2 ** 9 = 512


# ✅ Prawda.

# The right argument of the % operator cannot be zero.

# Operator modulo % zwraca resztę z dzielenia.

# Jeśli próbujesz podzielić przez zero, Python rzuci ZeroDivisionError.

# Przykład:

# 5 % 0  # ZeroDivisionError


# ✅ Prawda.

# Addition precedes multiplication.

# W Pythonie obowiązuje standardowa kolejność działań: mnożenie i dzielenie mają wyższy priorytet niż dodawanie i odejmowanie.

# Przykład:

# 2 + 3 * 4  # najpierw 3*4=12, potem 2+12=14


# ✅ Fałsz.

# Podsumowanie: prawdziwe stwierdzenia to:

# The ** operator uses right-sided binding.

# The right argument of the % operator cannot be zero.