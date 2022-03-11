data = [(10,25), (30, 45), (0,35)]

print(sorted(data,key=lambda x:x[1]))

op = data[0][1] - data[0][0]
for i in range(1, len(data)):
    # print(data[i])
    if data[i][0] < data[i-1][1]:
        starttime = data[i-1][1]
    else:
        starttime = data[i][0]
    # print(starttime)
    op += (data[i][1] - starttime)

print(op)


###Flatten List
# test = [1, 2, [3, 4, [5], [6, 7, [8, [9]]]]]
#
# op = []
#
#
# def flat(lst):
#     for i in lst:
#         if isinstance(i, list):
#             flat(i)
#         else:
#             op.append(i)
#     return op
#
#
# print(flat(test))
