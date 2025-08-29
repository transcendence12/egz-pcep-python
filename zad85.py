x = 2
y = 1
x *= y + 1
print(x)



# 🔎 Co się dzieje:

# x = 2
# → zmienna x ma wartość 2

# y = 1
# → zmienna y ma wartość 1

# x *= y + 1
# Tutaj działa operator *= (mnożenie i przypisanie).
# To jest skrót dla:

# x = x * (y + 1)


# 🔥 I teraz najważniejsze: najpierw oblicza się y + 1:

# y + 1 = 1 + 1 = 2

# Potem:

# x = 2 * 2 = 4

# 🟢 Wynik:
# 4


# *= to też operator, ale należy do grupy tzw. operatorów przypisania.
# A operator + (dodawanie) ma wyższy priorytet niż *= – dlatego Python najpierw policzył y + 1, a potem dopiero wykonał *=.