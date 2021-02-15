# inp = 'tacCat'
# op = inp
#
# def substr(stri, key, pos):
#     while key in stri:
#         there = stri.find(key)
#         if there != -1:
#             if pos == there:
#                 stri = stri[pos + 1:]
#             else:
#                 stri = stri[:there]
#     return stri
#
#
# for i in range(len(inp)):
#     # print(inp[i])
#     if inp[i].islower():
#         fnd = inp[i].upper()
#     else:
#         fnd = inp[i].lower()
#     if fnd in op:
#         continue
#     else:
#         op = substr(op, inp[i], i)
#         # print(op)
#
# print(op)
# # print(substr('zABaazz', 'z', 0))
#


inp = 'aAzBabz'


