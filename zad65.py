# You develop a Python application for your company.

# A list named employees contains 200 employee names, the last five being company management. You need to slice the list to display all employees excluding management.

# Which code segments can you use? (Choose two.)

# employees[1:-5]
# employees[0:-5]
# employees[:-5]
# employees[0:-4]
# employees[1:-4]



# Treść:

# employees → lista 200 elementów (indeksy od 0 do 199).

# Ostatnie 5 elementów to management (employees[195:200]).

# Chcemy wyświetlić wszystkich oprócz tych ostatnich pięciu → czyli elementy z indeksów 0 .. 194.

# Analiza opcji:

# employees[1:-5]

# zaczyna od indeksu 1, więc pomija pierwszego pracownika.

# Niepoprawne ❌

# employees[0:-5]

# zaczyna od 0, kończy 5 elementów przed końcem.

# To daje employees[0..194].

# Poprawne ✅

# employees[:-5]

# shorthand, to samo co powyżej (start domyślnie 0).

# Wynik: employees[0..194].

# Poprawne ✅

# employees[0:-4]

# kończy 4 elementy przed końcem → employees[0..195].

# Czyli zostaje jeden z managerów.

# Niepoprawne ❌

# employees[1:-4]

# zaczyna od indeksu 1 i kończy 4 przed końcem.

# Pomija pierwszego pracownika i zostawia jednego managera.

# Niepoprawne ❌

# ✅ Prawidłowe odpowiedzi:

# employees[0:-5]

# employees[:-5]