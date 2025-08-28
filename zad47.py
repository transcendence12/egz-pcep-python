data = [10, 2, 1, 7, 5, 6, 4, 3, 9, 8]

# insert your code here
def find_high_low(nums):
    nums.sort()
    return nums[-1], nums[0]
    
high, low = find_high_low(data)

print(
    ('The highest number is {}' + 
    'and the lowest number is {}.').format(high, low)
)

# Funkcja find_high_low(nums) sortuje listę nums.

# nums.sort() sortuje listę rosnąco.

# nums[-1] to największy element (ostatni po sortowaniu).

# nums to najmniejszy element (pierwszy po sortowaniu).

# return nums[-1], nums zwraca właśnie największy i najmniejszy element — dokładnie to, czego wymaga polecenie (najwyższy: 10, najniższy: 1)