# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)


n = 50
visits = []
for i in range(n):
    if i > 1:
        op = visits[i-1] + visits[i-2]
        visits.append(op)
    else:
        visits.append(1)
        # print(visits)

print(visits)