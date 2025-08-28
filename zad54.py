data1 = (1,2)
data2 = (3,4)

[print(sum(x)) for x in [data1 + data2]]

# 1️⃣ data1 + data2

# data1 i data2 to krotki (1,2) i (3,4).

# Operator + łączy krotki, tworząc nową:

# data1 + data2  # (1, 2, 3, 4)

# 2️⃣ [data1 + data2]

# Tworzysz listę z jedną krotką:

# [(1, 2, 3, 4)]

# 3️⃣ List comprehension [print(sum(x)) for x in ...]

# Iterujesz po liście z jedną krotką:

# for x in [(1, 2, 3, 4)]:
#     print(sum(x))


# sum(x) liczy sumę elementów krotki:

# sum((1, 2, 3, 4)) = 10


# print() drukuje wynik od razu, a list comprehension tworzy dodatkową listę z wartościami None (bo print() zwraca None).

# 4️⃣ Wynik na ekranie
# 10


# Jeśli sprawdzisz wynik samego wyrażenia [print(sum(x)) for x in [data1 + data2]], to w Pythonie zwróci [None], ale drukuje tylko 10.

# 🔑 Podsumowanie

# data1 + data2 → łączy krotki

# [data1 + data2] → lista z jednym elementem (tą krotką)

# [print(sum(x)) for x in ...] → iteruje, sumuje elementy krotki i drukuje, tworząc listę [None] w tle

# Efekt na ekranie: 10






# 1️⃣ Co robi list comprehension?

# Składnia:

# [wyrażenie for element in lista]


# Zawsze tworzy nową listę, której elementami są wyniki wyrażenia.

# W tym przypadku wyrażenie to print(sum(x)).

# 2️⃣ print() zwraca None

# Funkcja print() drukuje coś na ekran, ale nie zwraca wartości, tylko None.

# Przykład:

# result = print(10)  # wydrukuje 10
# print(result)       # -> None

# 3️⃣ Jak działa Twoja list comprehension

# data1 + data2 → (1,2,3,4)

# [data1 + data2] → [(1,2,3,4)]

# Iteracja: for x in [(1,2,3,4)]

# sum(x) → 10

# print(sum(x)) → drukuje 10 i zwraca None

# List comprehension zbiera te zwracane wartości (tu tylko None) i tworzy listę:

# [None]

# 4️⃣ Co widzisz na ekranie

# Python najpierw wykonuje print(sum(x)) → na ekranie pojawia się 10

# W tle powstaje [None], ale nie jest nigdzie przypisana ani drukowana, więc nie widzisz jej.

# 🔑 Wniosek

# Na ekranie: 10

# Wartość zwracana przez list comprehension: [None]
