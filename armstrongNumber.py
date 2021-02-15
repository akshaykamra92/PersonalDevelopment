# n=153
# a=list(map(int,str(n)))
# print(a)
# b=list(map(lambda x:x**3,a))
# print(b)
# if(sum(b)==n):
#     print("The number is an armstrong number. ")
# else:
#     print("The number isn't an arsmtrong number. ")
#
sentence1 = 'We are in city'
sentence2 = 'The city was hit n life life'


def solution(sentence1, sentence2):
    set1 = set(sentence1.split())
    set2 = set(sentence2.split())

    return ((set1 ^ set2)), ((set1 & set2))  # ^ A.symmetric_difference(B), & A.intersection(B)


print(solution(sentence1, sentence2))