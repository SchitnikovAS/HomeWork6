my_dict = {'Ilia':1992, 'Olia':1993, 'Kolia':2001, 'Nina':[2003,'girl','she is loves Ilia']}
print(my_dict)
print(my_dict.get('Kolia'))
print(my_dict.get('Vasia', 'Такого ключа не существует!'))
my_dict.update({'Valia':1997,
                'Dima':1999})
pair = my_dict.pop('Olia')
print(pair)
print(my_dict)
my_set = {1, (1,2,2,4), 2, True, 3, 2,'Cool', 2.2, 3, True, 1, 'Cool', 1, (1,2,2,4)}
print(my_set)
my_set.add(11111111)
my_set.add("Hello, I'm new element!")
my_set.discard((1,2,2,4))
print(my_set)