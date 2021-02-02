n = 10
ops = ['L', 'L', 'C100', 'L','C3']

test = [0 for i in range(n)]
# print test and check ki woh bani kya
for i in ops:
    if i == 'L':
        ind = test.index(0)
        test[ind] = 1
    else:
        ip = int(i[1:])
        if ip > len(test)-1:
            print('skipped')
            continue
        else:
            test[ip] = 0
final = ''.join(map(str, test))
# print(final.join(str(test)))
print(final)