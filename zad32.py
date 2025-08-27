nums = []
vals = nums
vals.append(1)
print(nums)
print(vals)

# vals is longer than nums
# nums and vals are of the same length   - PRAWIDŁOWA odpowiedź
# nums is longer than vals


# 🔑 Wniosek

# W Pythonie listy są mutowalne, a przypisanie = tworzy referencję do tego samego obiektu, nie kopię.

# Jeśli chcesz mieć niezależną kopię listy, użyj np.:

# vals = nums.copy()
# # lub
# vals = list(nums)