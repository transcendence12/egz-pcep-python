#  Which function does in-place reversal of objects in a list?

# list.sort([func])
# list.pop(obj=list[-1])
# list.remove(obj)
# list.reverse()

# Wyjaśnienie opcji:

# list.sort([func]) → sortuje elementy listy, ale nie odwraca ich (chyba że użyjesz reverse=True, ale to inna historia).

# list.pop(obj=list[-1]) → usuwa i zwraca ostatni element listy (domyślnie list[-1]), nie odwraca listy.

# list.remove(obj) → usuwa pierwsze wystąpienie elementu obj z listy.

# ✅ list.reverse() → odwraca kolejność elementów w tej samej liście (in-place).

# A jeśli chcesz nową odwróconą listę bez zmiany oryginału, używasz reversed(nums) albo nums[::-1].