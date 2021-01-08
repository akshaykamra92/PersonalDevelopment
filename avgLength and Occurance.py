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
    wordsl = words.split(' ')
    uniqueWords = set(wordsl)
    for i in uniqueWords:
        print(i + " - " + str(wordsl.count(i)))


def uniquewords(words, words2):
    uniquelist = []
    jointsent = words+' '+words2
    wordlist = jointsent.split(' ')
    unique = set(wordlist)
    for i in unique:
        if jointsent.count(i) == 1:
            uniquelist.append(i)
    return uniquelist


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
                test[i] = test[i-1]
                final.append(test[i])
                continue
            final.append(test[i])
        return final


test = [None,1]
print(replaceNone(test))







