List2 = [3,1,2]
List1 = [1,1]

final = []
len1 = len(List1)
len2 = len(List2)
if len1 > len2:
    test1 = List2
    test2 = List1
else:
    test1 = List1
    test2 = List2
for value in test1:
    if value in test2:
        final.append(value)
        test2.remove(value)

print(final)