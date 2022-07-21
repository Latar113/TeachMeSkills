def gen(a):
    next_element = 1
    while True:
        next_element *= a
        yield next_element


gen = gen(5)
print(next(gen))
print(next(gen))
print(next(gen))