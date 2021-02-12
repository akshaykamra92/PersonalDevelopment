#Find Avg length of words in sentence
#Find occurance of words
#Find Uncommon words from 2 sentences
#Replace None with Prev value

words = 'Hello my name is Akshay Kamra Akshay None'
# words = 'Akshay'
words2 = "this is yellow Hello my name"


def avgLen(sent):
    wordlist = sent.split(' ')
    lengths = [len(i) for i in wordlist]
    if len(wordlist) == 0:
        return 0
    elif len(wordlist) == 1:
        return float(lengths[0])
    else:
        avg = float(sum(lengths)/len(wordlist))
        return avg


def wordCounter(words):
    from collections import Counter
    op = Counter(words.split(' '))
    return op.most_common()[3]

    # wordsl = words.split(' ')
    # uniqueWords = set(wordsl)
    # for i in uniqueWords:
    #     print(i + " - " + str(wordsl.count(i)))

# s1 = 'My name is Akshay Akshay'
# print(wordCounter(s1))
string = 'Hello'
print(string.replace('l','a'))

def uniquewords(words, words2):
    set1 = set(words.split(' '))
    set2 = set(words2.split(' '))
    unq = set1 ^ set2
    return list(unq)
    # uniquelist = []
    # jointsent = words+' '+words2
    # wordlist = jointsent.split(' ')
    # unique = set(wordlist)
    # for i in unique:
    #     if jointsent.count(i) == 1:
    #         uniquelist.append(i)
    # return uniquelist

# s1 = 'My name is Akshay'
# s2 = 'my name is Karishma'
# print(uniquewords(s1,s2))

def replaceNone(test):
    final = []
    if len(test) == 1:
        return test
    else:
        for i in range(len(test)):
            if i == 0 and test[i] is None:
                final.append(None)
                continue
            if test[i] is None:
                # test[i] = test[i-1]
                final.append(final[i-1])
                continue
            final.append(test[i])
        return final, test


# s = input('Number if instances ')
# ll = []
# for i in range(int(s)):
#     a = input('Enter sent ')
#     ll.append(str(a))
# # print(ll)
# dic = {}
# for i in ll:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1
#
# print(len(dic.keys()))
# for i in list(dic.values()):
#     print(i, end=' ')
# import numpy
# inp = [1,2,3,4]
# final = []
# for i in range(len(inp)):
#     ll = [inp[:i] + inp[i+1:]]
#     final.append(numpy.prod(ll))
# print(final)
# a,*b, c = "foo:boo:coo:doo".split(":")
# # print("a:", a, "b:", b, "c:",c)
# print(a,b,c)
#
# test = [1,2,3,4]
# print(test[:])