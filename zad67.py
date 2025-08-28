x = [1,2,3,4,5,6,7,8,9]
x[::2] = 10, 20, 30, 40, 50, 60
print(x)



# Opcje:

# [1, 10, 3, 20, 5, 30, 7, 40, 9, 50, 60]
# [1, 2, 10, 20, 30, 40, 50, 60]
# The code is erroneous.
# [10, 2, 20, 4, 30, 6, 40, 8, 50, 60]



# Krok 1 – Co oznacza x[::2]?

# ::2 oznacza: bierz co drugi element, zaczynając od indeksu 0.

# Czyli wybieramy elementy na pozycjach 0, 2, 4, 6, 8.

# Z listy:

# [1, 2, 3, 4, 5, 6, 7, 8, 9]
#  ↑     ↑     ↑     ↑     ↑
#  0     2     4     6     8


# Wynik: [1, 3, 5, 7, 9]

# Krok 2 – Przypisanie

# Przypisujemy do tych 5 elementów:

# 10, 20, 30, 40, 50, 60


# Problem: prawa strona ma 6 elementów, a lewa strona tylko 5 slotów.

# Krok 3 – Czy Python to zaakceptuje?

# ❌ Nie.
# W slice assignment długość obu stron musi być taka sama.

# Dlatego dostaniemy błąd:

# ValueError: attempt to assign sequence of size 6 to extended slice of size 5


# ✅ Poprawna odpowiedź z opcji:
# The code is erroneous.