def factorial(n: int) -> int:
    print('init', n)
    if n < 2:
        print('fact, n')
        return 1
    else:
        res = factorial(n - 1) * n
        print('fact', n, res)
        return res


print(factorial(3))
