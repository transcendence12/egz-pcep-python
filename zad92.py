# What is the expected output of the following code?

print (1 // 2 * 3)

# 4.5
# 0.16666666666666666
# 0.0
# 0 - PRAWIDŁOWA ODPOWIEDŹ






# // to operator dzielenia całkowitego (floor division).

# 1 // 2 = 0, bo dzielenie całkowite 1 przez 2 daje 0.

# Następnie * 3

# 0 * 3 = 0

# Wynik jest integerem (0), bo wszystkie operacje to liczby całkowite.

# ✅ Odpowiedź:

# 0


# Nie jest to ani float, ani ułamek, tylko zwykłe 0.




# W Pythonie mnożenie (*) i dzielenie (/ lub //) mają ten sam priorytet i są wyliczane od lewej do prawej (left-to-right), jeśli występują w tym samym wyrażeniu.

# Przykład:

# 8 / 4 * 2


# Krok po kroku (od lewej):

# 8 / 4 → 2.0

# 2.0 * 2 → 4.0

# Podobnie dla floor division:

# 7 // 2 * 3


# 7 // 2 → 3

# 3 * 3 → 9

# Więc ani mnożenie, ani dzielenie nie „przeważa” – liczy się kolejność od lewej do prawej.
