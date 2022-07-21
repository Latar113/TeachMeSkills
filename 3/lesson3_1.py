chislo = input('Введите число: ')

if chislo.count('.') <= 1 and chislo.count('-') <= 1:
    if chislo.replace(".", "").replace("-", "").isdigit():
        chislo = float(chislo)

        if chislo > 0:
            print('Положительно')
        elif chislo < 0:
            print("Отрицательно")
        elif chislo == 0:
            print('Ноль')
    else:
        print('Введите число!')
