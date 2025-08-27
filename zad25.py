data = {'name':'Peter', 'age':30}
person = data.copy()
print(id(data)==id(person))

# False


# = → przypisanie referencji (obie zmienne wskazują na ten sam obiekt)

# .copy() → tworzy nowy obiekt z takimi samymi wartościami

# Dlatego id(data) != id(person)