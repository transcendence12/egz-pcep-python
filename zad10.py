d = {}
d[1] = 1
d['1'] = 2
d[1] += 1

sum = 0
for k in d:
    sum += d[k]

print(sum)




# {1: 1, '1': 2}

# d[1] += 1
# Czyli d[1] = d[1] + 1 → 1 + 1 = 2.

# Słownik wygląda teraz tak:
# {1: 2, '1': 2}

# k = 1 → sum = 0 + d[1] = 0 + 2 = 2

# k = '1' → sum = 2 + d['1'] = 2 + 2 = 4