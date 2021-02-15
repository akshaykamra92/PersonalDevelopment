from collections import Counter
statemnt =' Hello this is a new world  hello and welcome in this new world here'
states = statemnt.split()
# fruits = ['apple', 'orange', 'apple',]
Word = Counter(states)
print(Word)
final = Word.most_common()[-2]
print(final)


