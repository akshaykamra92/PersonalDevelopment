inp = 'AKSHAY'
aks = 0 #vowels
kar = 0 #consonants
i = 0
j = 1
# while i <= len(inp):
#     # print(i)
#     while j <= len(inp):
#         curr = inp[i:j]
#         # print(curr)
#         if curr[0] in ['A', 'E', 'I', 'O', 'U']:
#             aks += 1
#         else:
#             kar += 1
#         j += 1
#     i += 1
#     j = i+1
def var(i,inp):
    while i <= len(inp):
        print(inp[0:i])
        i += 1
print('vowels score ', aks)
print('consosnat score ', kar)
