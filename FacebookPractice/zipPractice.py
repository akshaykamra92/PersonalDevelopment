from functools import reduce

ll = [1, 2, 3, 4, 5, 6]

op = [sum(val) for val in zip(ll, ll[1:])]
print(op)

lis = [[1,2], [3,4], [5,6]]

test = list(sum(x) for x  in zip(*lis))
print(test)