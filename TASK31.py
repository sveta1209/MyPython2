print(2 == 3)
s = [1, 2.0, True, None, "Some string", {"key": "value"}, [{"a":"b"}, {"c": 25}]]
print(s)

s.remove(1)
print(s)
# Как удалить элемент по индексу(номеру позиции в списке):
del s[1]
print(s)

x = 7
while x < 10:
    print(x)
    x = x+1

test_gen = [x for x in range(2, 16)]
print(test_gen)


gladiator = {"name": "Gladiator", "year": 2000, "actors": ["Russell Crowe", "Joaquin Phoenix"], "sequels": []}
bladrunner = {"name": "Bladerunner", "year": 1982, "actors": ["Harrison Ford", "Rutger Hauer"],
                  "sequels": ["Bladerunner 2049"]}
once_in_america = {"name": "Once upon a time in America", "year": 1984, "actors": ["Robert De Niro", " Joe Pesci"],
                       "sequels": []}
spiderman_2 = {"name": "Spider-Man 2", "actors": ["Tobey Maguire"], "year": 2004, "sequels": ["Spider mna 3"]}
nice_guys = {"name": "The Nice Guys", "year": 2016, "actors": ["Russell Crowe", "Ryan Gosling"], "sequels": []}

    # Пример списка со словарями
movies = (gladiator, bladrunner, once_in_america, spiderman_2)
print(movies)

"""""
    Часто нам нужно достать один или несколько элементов из коллекции (последовательности).
    И мы можем не знать индекса этого элемента, 
    да и задавать в ручную индекс довольно неудобно.
    Для этого нам нужен инструмент, позволяющий перебирать коллекции.
    Этот инструмент - цикл for 
    Он идет по ПОСЛЕДОВАТЕЛЬНОСТЯМ (тупль, список, сет),
    и для этого похода использует то, что называется ИТЕРАТОРОМ
    ИТЕРАТОР это переменная, которая идет ВНУТРИ цикла 
    и принимает значения элементов один за другим.
"""
""""
	Внутри цикла мы можем то же, что и во всем остальном коде,
	только еще и имея доступ к значениям ВНУТРИ цикла.
	Например так: 
	наш итератор movie принимает последодвательно значения в тупле movies
	И каждый новый шаг - movie будет становится одним из словарей-фильмов.
"""
for movie in movies:
    print(movie["name"])
    print(movie)

# Соотетственно мы можем обращаться к переменной как к словарю.


for x in [1, 2, 3]:
        print(x)
        if x == 2:
                 break
