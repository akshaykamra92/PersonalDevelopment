t = [(2,1), (1,1), (2,4), (2,6), (7,5), (6,4)]
res = {}

for i,j in t:
    res.setdefault(j, []).append(i)
print(sorted(res))