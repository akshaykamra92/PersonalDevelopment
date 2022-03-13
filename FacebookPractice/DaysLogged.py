web = [1, 4, 6, 7]
ios = [2,3,6,7]
andr = [1,2,7]

logging = {}

check = ['andr', 'ios', 'web']


def logcreate(arr):
    for day in arr:
        logging.setdefault(day, []).append(1)


def totalling(dic):
    output = [sum(dic[i]) if i in dic else 0 for i in range(1,8)]
    return output


for typ in check:
    case = eval(typ)
    logcreate(case)
print(logging)
print(totalling(logging))