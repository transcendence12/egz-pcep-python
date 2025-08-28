#  What code would you insert instead of the comment to obtain the expected output?

# Expected output: a, b, c

dictionary = {}
my_list = ['a', 'b', 'c', 'd']

for i in range(len(my_list) -1):
    dictionary[my_list[i]] = (my_list[i], )

for i in sorted(dictionary.keys()):
    k = dictionary[i]
    # insert your code here



# opcje:
# print(k[0])
# print(k)
# print(k['0'])
# print(k["0"])


# Krok po kroku:

# Pierwsza pętla for i in range(len(my_list) -1)

# len(my_list) = 4, więc range(3) → i = 0, 1, 2

# Tworzymy słownik:

# dictionary = {
#   'a': ('a',),
#   'b': ('b',),
#   'c': ('c',)
# }


# Druga pętla for i in sorted(dictionary.keys())

# Klucze to 'a', 'b', 'c' (posortowane → w tej samej kolejności).

# Dla każdego klucza i, pobieramy wartość:

# k = ('a',)

# k = ('b',)

# k = ('c',)

# Czyli k to krotka jednoelementowa.

# Co chcemy wypisać?

# Oczekiwany output:

# a
# b
# c


# A k to np. ('a',) → żeby dostać "a", trzeba się odwołać do pierwszego elementu krotki.

# Opcje:

# print(k[0]) ✅ → daje "a", "b", "c" (dokładnie to, co trzeba).

# print(k) ❌ → da ('a',), ('b',), ('c',) (z nawiasami).

# print(k['0']) ❌ → błąd (TypeError, bo '0' to string, a k to tuple).

# print(k["0"]) ❌ → to samo, błąd.

# ✅ Prawidłowa odpowiedź:
# print(k[0])