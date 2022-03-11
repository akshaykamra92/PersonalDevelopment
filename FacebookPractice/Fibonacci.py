test = ['Apple', 'ple', 'something', 'thin']
matching = []
matcher = []
for i in range(len(test)):
    for val in test[i+1:]+test[:i]:
        if val.upper() in test[i].upper():
            matching.append(test[i])
            matcher.append(val)

print(matching)
print(matcher)

