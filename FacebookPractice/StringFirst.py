test = [1,2,3,4,5]
i =0
final = []
for i in range(len(test)):
    print(i)
    print(test)
    if i % 2 == 0:
        final.append(test[0])
        test.remove(test[0])
    else:
        final.append(test[::-1][0])
        test.remove(test[::-1][0])
print(final)