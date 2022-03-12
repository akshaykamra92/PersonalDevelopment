def fib(n, dic):
    if n in dic:
        return dic[n]
    if n <= 2:
        return 1
    dic[n] = fib(n - 1, dic) + fib(n - 2, dic)
    return dic[n]


visits = {}
print(fib(7, visits))

print(visits)