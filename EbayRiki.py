#Case when two lists have same length

l1 = [2,-2,5,3]
l2 = [1,5,-1,1]

counter = 0
# for i in range(len(l1)):
#     for j in range(len(l2)):
#         if i <= j:
#             if l1[i]-l2[j] == l1[j]-l2[i]:
#                 print(i,j)
#                 counter += 1
#
[counter += 1 if l1[i]-l2[j] == l1[j]-l2[i] for i in range(len(l1)) for j in range(len(l2))]
