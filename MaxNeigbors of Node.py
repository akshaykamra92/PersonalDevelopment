import collections


# d = collections.defaultdict(int)
# for i in neigh:
#     if len(i) == 2:
#         d[i[0]] += 1
#         d[i[1]] += 1
# print(d)
# print(max(d))
def neighborsCount(neigh):
    dictfinal = {}
    size = []
    ind = 0
    output = []
    for item in neigh:
        size.append(len(item))
    if max(size) > 1:
        for i in neigh:
            if len(i) > 1:
                for inp in i:
                    if inp not in dictfinal:
                        dictfinal[inp] = 1
                    else:
                        dictfinal[inp] = dictfinal[inp] + 1

                k = list(dictfinal.keys())
                v = list(dictfinal.values())
        maxval = max(v)
        for val in v:
            if val == maxval:
                output.append(k[ind])
            ind += 1
        # return k[v.index(max(v))]
        return output
    else:
        return 'No Neighbors detected'


neigh = [['A'], ['A', 'B'], ['A', 'C'], ['B', 'D', 'C'], ['C', 'B']]

# print(neighborsCount(neigh))
def friends(inp):
    frdlist = {}
    for friends in inp:
        if len(friends) > 1:
            for fr in friends:
                if fr in frdlist:
                    frdlist[fr] += len(friends)-1
                else:
                    frdlist[fr] = len(friends)-1
    nodes = list(frdlist.keys())
    num = list(frdlist.values())
    for i, x in enumerate(num):
        if x == max(num):
            print(nodes[i])
    print(frdlist)
    # print(i for i, x in enumerate(nodes) if x == max(num))


friends(neigh)

