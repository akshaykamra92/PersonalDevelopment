test = 'Hello My name is Akshay Kamra'
percent = 50


def splitter(wrd, pcnt):
    brk = int(len(wrd) * (pcnt/100))
    return wrd[:brk] + ' ' + wrd[brk:]


words = test.split()
op = ''
for word in words:
    out = splitter(word, percent)
    op += out+' '
