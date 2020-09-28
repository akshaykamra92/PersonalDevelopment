stat = 'The Sky is Blue'
test = stat.split()
rev = list(reversed(test))
final = ''
# for i in range(len(rev)):
#     final = final + rev[i] + ' '
# print(final)
print(" ".join(rev))