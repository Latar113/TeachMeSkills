def gen3(start, limit):
    for _ in range(limit):
        yield start
        start = start * 5

a = gen3(1, 5)
print(next(a))
print(next(a))
print(next(a))


for i in gen3(1, 5):
    print(i)

print('-'*10)

def gen_geo(q):
    next_element = 1
    while True:
        next_element *= q
        yield next_element

gen = gen_geo(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


print('-'*10)

def geo(q, finish):
    geom_progress = (b * q for b in range(1, finish))
    for b in geom_progress:
        yield b


g = geo(2, 6)
print(next(g))
print(next(g))