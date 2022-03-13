val = 699
# add 5 and see what is largest
strip = str(val)
if val < 0:
    # minus = strip[0]
    neg = 1
    strip = strip[1:]
    maxval = int(strip+'9')
else:
    neg = 0
    maxval = int(val)
for i in range(len(strip)+1):
    op = strip[:i] + '5' + strip[i:]
    if neg == 0 and maxval < int(op):
        maxval = int(op)
    elif neg == 1 and maxval > int(op):
        maxval = int(op)
    else:
        continue

if neg == 1:
    print(int('-'+str(maxval)))
else:
    print(maxval)
