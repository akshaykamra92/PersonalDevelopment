#Flatten List of Lists to a List
#Validate IP Address


test = ['A','B',['C'], ['D','E',['F','G']]]
final = []
def ll(data):
    for ip in range(len(data)):
        append(data[ip])


def append(inp):
    # final = []
    if isinstance(inp,str):
        final.append(inp)
        print(final)
    else:
        ll(inp)


# ll(test)

ip = '192.168.9.1'
import re
quart = ip.split(".")
for ip in quart:
    x = re.findall(r'^[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-5][0-5]\.{3}',ip)
    print(x)
# print(quart)
# x = all(0 < len(ind) < 4 and 0 <= int(ind) <= 255 for ind in quart)
# print(x)
#     x = re.findall(r'^[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-5][0-5]',ip)

test = [3,1,3,4,5,6,6]
# for i in test:
#     print(i)
sumi = 5
elements = []
for i in test:
    # print(i)
    if i < sumi:
        find = sumi - i
        if find in test:
            elements.append((i, find))
            test.remove(i)
            test.remove(find)
        else:
            pass
            # print('Pair not available')
    else:
        pass
    # print(i)
print(test)
print(elements)



