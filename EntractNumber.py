

def extract(ip):
    numberextract = ''
    for i in ip:
        if i.isdigit():
            numberextract = numberextract+i
        else:
            break
    if numberextract == '':
        return 0
    else:
        return numberextract


def findNumber(strin):
    strin = strin.lstrip()
    isNegative = 0
    if strin[0] == '-':
        isNegative = 1
        strin = strin[1:]
        nop = extract(strin)
    else:
        posop = extract(strin)
    if isNegative == 1:
        final = 0-int(nop)
    else:
        final = int(posop)

    print(final)

# inp = 'Enter a string of your choice'
#
# inp = inp.lstrip()
findNumber('   444asd')


