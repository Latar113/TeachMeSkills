#одинаковые данные и идентификаторы

a = 1
b = 1
c = 1
print(id(a), id(b), id(c))

#Сделать id разными
a = str(a)
b = str(b)
c = str(c)
print(id(a), id(b), id(c))

#одинаковые данные разные идентификаторы
v = [1]
x = [1]
print(id(v), id(x))

#Сделать id одинаковыми
v = x
print(id(v), id(x))