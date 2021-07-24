# def summ(a,b):
#     x = a+b
#     if x >= 1:
#         return 1
#     else:
#         return 0


test = ['ios', 'web']
ios = [1,1,1, 0, 0, 1, 0]
web = [1,0,0, 0, 0, 0, 1]
android = [0,0,0, 1, 1, 1, 1]

# for fn in test:
#     control = list(map(summ, control, eval(fn)))
#
# print(control)
vals = list(eval(i) for i in test)
final = [1 if sum(comb) >= 1 else 0 for comb in zip(*vals)]
print(final)
