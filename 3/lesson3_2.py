stroka = input('Введите строку: ')
chars = []
count_chars = []
max_count = 1

for g in stroka:
    if g.isalpha():
        count = stroka.count(g)
        if max_count < count:
            max_count = count
        if g not in chars and g.isalpha():
            chars.append(g)
            count_chars.append(count)
if len(chars) == 0:
    print('Вы ввели не строку!')
else:
    for i in range(len(chars)):
        print(f'| {chars[i]} | {count_chars[i]: <{len(str(max_count))}} |')
