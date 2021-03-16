def summ(a,b):
    x = a+b
    if x >= 1:
        return 1
    else:
        return 0


test = ['ID', 'VAL']
ID = [1,1,1]
VAL = [1,0,0]
control = [0,0,0]

for fn in test:
    control = list(map(summ, control, eval(fn)))

print(control)
