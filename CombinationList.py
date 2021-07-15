
#Find the sum of combinations for list 1 and see if sum is present in Tests, if present then return True else False

lsts = [1, 2, 3, 4]
test = [5, 9, 10]
from itertools import combinations


out = list(combinations(lsts, 2))
print(out)
output = False
for item in out:
    if item[0] + item[1] in test:
        output = True
        break

if output is True:
    print(True)
else:
    print(False)