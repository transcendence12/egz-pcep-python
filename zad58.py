a = [1,2,3,4,5]
print(a[3:0:-1])



# 1️⃣ Indeksy w a:
# a = [1,   2,   3,   4,   5]
#       0    1    2    3    4

# 2️⃣ Co oznacza a[3:0:-1]?

# Slicing ma składnię:

# lista[start:stop:step]


# start = 3 → zaczynamy od elementu o indeksie 3, czyli 4

# stop = 0 → zatrzymujemy się przed indeksem 0 (0 nie jest włączony!)

# step = -1 → poruszamy się wstecz

# 3️⃣ Jak to działa krok po kroku:

# startujemy od a[3] = 4

# następny krok wstecz → a[2] = 3

# następny krok wstecz → a[1] = 2

# kolejny krok wstecz byłby a[0] = 1, ale STOP = 0 wyklucza ten element

# ➡️ dlatego zatrzymujemy się przed indeksem 0.

# 4️⃣ Wynik:
# [4, 3, 2]


# ✅ Dlaczego nie ma 1?
# Bo w slice a[start:stop:step], stop zawsze jest wyłączony.
# Tutaj stop=0, więc element o indeksie 0 (czyli 1) nie wchodzi do wyniku.

# 👉 Gdybyś chciała, żeby było [4,3,2,1], trzeba zrobić tak:

# print(a[3::-1])   # stop = domyślnie None → idziemy aż do początku listy


# Output:

# [4, 3, 2, 1]