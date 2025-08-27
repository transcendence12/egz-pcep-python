str1 = 'Peter'
str2 = str1[:]
print(str1)
print(str2)

print(str1 == str2)   # True  (mają tę samą wartość)
print(str1 is str2)   # False (to różne obiekty w pamięci)

# ✨ Wniosek:

# ✔ str1 i str2 to różne obiekty (różne stringi), ale mają taką samą wartość.
# ❌ Nie są „różnymi nazwami tego samego stringa” (to byłoby prawdą, gdybyśmy zrobili str2 = str1).