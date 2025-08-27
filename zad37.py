t1 = (1,4,9)
t2 = ('A', 'D', 'Z')
t3 = (True, False, None)
t4 = (5.0, 7.5, 9.9)
t1, t3 = t2, t4
print(t1) 

# ('A', 'D', 'Z')

# Wniosek

# Przypisanie wielokrotne (a, b) = (x, y) pozwala jednocześnie zmienić kilka zmiennych.

# Wartości po prawej stronie przypisania są przypisywane do zmiennych po lewej w kolejności.

# Poprzednie wartości t1 i t3 są nadpisywane i tracone (chyba że były przechowywane gdzie indziej).