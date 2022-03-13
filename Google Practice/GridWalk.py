def walk(n,m, visits):
    steps = 0
    # print(visits)
    if (n,m) in visits:
        return visits[(n,m)]
    if n == 1 and m == 1:
        return 1
    if n == 0 or m == 0:
        return 0
    else:
        visits[(n,m)] = walk(n-1,m, visits) + walk(n,m-1, visits)
        return visits[(n,m)]


visits = {}
n = 3
m = 3
print(walk(n,m, visits))
# print(len(visits.keys()))
print(visits)

