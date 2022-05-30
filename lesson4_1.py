def go(text: str):
    if text.count('.') <= 1 and text.count('-') <= 1 and text.replace('.', '').replace('-', '').isdigit():
        if text[0] == '-' and text[1].isdigit():
            return True
        elif text.replace('.', '').isdigit() and text[0] != '.':
            return True
        else:
            return False
    else:
        return False


line = input('Введите число!: ')
if go(line):
    line = float(line)
    if line > 0:
        print('Положительное')
    elif line < 0:
        print('Отридцательное')
    else:
        print('Ноль')
else:
    print('Введите число!')
