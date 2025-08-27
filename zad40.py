data = (1, ) * 3
data[0] = 2
print(data)

# Tutaj próbujesz zmienić element krotki pod indeksem 0.

# ALE: krotki w Pythonie są niemutowalne – nie można zmieniać ich elementów po utworzeniu.

# Dlatego pojawi się błąd:

# TypeError: 'tuple' object does not support item assignment

# print(data) - Ten wiersz w ogóle się nie wykona, bo program przerwie działanie w momencie błędu.