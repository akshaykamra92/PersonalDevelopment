input_list = ['cat', 'bat', 'rat', 'drat', 'dart', 'drab', 'monalisa']
word = '..t'
filteredList = []
if word in input_list:
    print(True)
elif word is None:
    print(False)
elif len(word) == 0:
    print(False)
else:
    for ip in input_list:
        if len(word) == len(ip):
            for i in range(len(word)):
                # print(i)
                if word[i] == ip[i] or word[i] == '.':
                    # print(word[i], ip[i])
                    if i == len(word)-1:
                        filteredList.append(ip)
                    continue
                else:
                    break

print(filteredList)
# wd = j= 0
# for i in range(len(filteredList)):
#     if word[j] == filteredList[i][j] or word[j] == '.':
#         j += 1
# if len(word) == 1 and word == '*':
#     print(input_list)