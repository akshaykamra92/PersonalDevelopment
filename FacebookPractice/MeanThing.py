a = [[3, 3, 4, 2],
     [4, 4],
     [4, 0, 3, 3],
     [2, 3],
     [3, 3, 3]]
means = []
for arr in a:
    if len(arr) == 1:
        means.append(arr[0])
    else:
        means.append(sum(arr)/len(arr))
print(means.index(3.0))