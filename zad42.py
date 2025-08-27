nums = [1,2,3]
vals = nums

# nums and vals are different lists?
# vals is longer than nums?
# nums and vals are different names of the same list?
# nums and vals have the same length?


# Co się dzieje?

# nums i vals wskazują na ten sam obiekt w pamięci (czyli na tę samą listę).

# Nie tworzysz kopii listy, tylko drugi alias (inna nazwa do tego samego miejsca w pamięci).

# Analiza odpowiedzi:

# "nums and vals are different lists" ❌
# → nieprawda, to ta sama lista.

# "vals is longer than nums" ❌
# → obie mają dokładnie tę samą długość.

# "nums and vals are different names of the same list" ✅
# → prawda, oba wskazują na ten sam obiekt.

# "nums and vals have the same length" ✅
# → też prawda, bo to ta sama lista.