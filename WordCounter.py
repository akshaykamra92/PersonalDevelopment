# Count words in sentence
from collections import Counter
# def wordCounter(string):
#     print("Enter string: ")
#     counts = {}
#     words = string.split()
#
#     # print(string)
#     for word in words:
#         if str.capitalize(word) in counts:
#             counts[str.capitalize(word)] += 1
#         else:
#             counts[str.capitalize(word)] = 1
#
#     return counts
def wordCount(s):
    m=' '
    i =0
    while i < len(s):
        if s[i].islower():
            if s[i].upper() not in s:
                print('first')
                print
                m=s[i+1:]
                # print(m)
                # print(s[i])
                if s[i] in m:
                    r = m.index(s[i])
                    s=m[:r]
                else:
                    s = m
                    # print("x",s)

        else:
            if s[i].lower() not in s:
                print('second')
                m = s[i + 1:]
                # print("m", m)
                if s[i] in m :
                    r = m.index(s[i])
                    s=m[:r]
                else :
                    s =m
                # print("x",s)

        i = i+1
    return s
# s='ABCD'
# print(s[:1])
# print(wordCount('tacoCat'))

list1 = ['CDaA', 'BA','AA']
print(sorted(list1,key=len))
