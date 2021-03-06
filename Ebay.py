import collections
# def test():
val = 'a:a,b:2,c:2'
x = val.split(',')
final = {}
for inp in x:
    keyval = inp.split(':')
    # print(keyval)
    if keyval[1] in final:
        if type(final[keyval[1]]) == list:
            final[keyval[1]].append(keyval[0])
        else:
            ll = []
            first = final[keyval[1]]
            second = keyval[0]
            ll.append(first)
            ll.append(second)
            final[keyval[1]] = ll
    else:
        final[keyval[1]] = keyval[0]

op = reversed(list(final.items()))
print(op)