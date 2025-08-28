nums = []
vals = nums[:]
vals.append(1)


# opcje:
# nums and vals are of the same length
# nums is longer than vals
# vals is longer than nums



# nums = []
# vals = nums[:]   # kopiujemy całą listę nums (shallow copy)
# vals.append(1)
# Krok po kroku:
# nums = []
# → nums to pusta lista.

# vals = nums[:]
# → operator [:] tworzy nową listę (kopię).
# Teraz mamy:

# nums → []
# vals → []
# (dwie różne listy w pamięci)

# vals.append(1)
# → dodajemy 1 do vals, a nums zostaje bez zmian:

# css
# Kopiuj
# Edytuj
# nums → []
# vals → [1]
# Wynik:
# nums ma długość 0

# vals ma długość 1

# ✅ Prawidłowa odpowiedź:

# vals is longer than nums

# ⚠️ Gdybyś zrobiła przypisanie bez slice:

# vals = nums
# vals.append(1)


# to wtedy obie listy wskazują na ten sam obiekt i wynik byłby:

# nums → [1]
# vals → [1]


# czyli "nums and vals are of the same length".