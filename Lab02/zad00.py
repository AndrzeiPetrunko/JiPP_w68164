numbers = [1,2,3,4,5,6,7,8,9]
numbers1 = [x ** 2 for x in numbers if x % 2 != 0]


#lista składana
def fun1(x):
    return x * x
numbers2 = list(map(lambda x: x * 2, numbers))
#map(funkcja(zwykła, anonimowa), iterowalna struktura)
#zwraca iterator
numbers3 = list(map(fun1, numbers))
#numbers2 i numbers3 są tworzone tak samo


#filter(warunek, struktura) - wybieranie elementów
def fun2(x):
    return x % 2 == 0
numbers4 = list(filter(fun2, numbers))
numbers5 = list(filter(lambda x: x % 2 == 0, numbers))


#reduce(funk, strukt)
from functools import reduce
max_liczba = reduce(lambda x, y: x if x > y else y, numbers)
wynik = reduce(lambda x, y: x + y, numbers)


b = 10
example = "2+2-1+b"
result = eval(example)
print(result)
#pojedyncze linijki

code = """
for i in range(3):
    print("witaj ",i)
"""
exec(code)
#wiecejjjjjjj

