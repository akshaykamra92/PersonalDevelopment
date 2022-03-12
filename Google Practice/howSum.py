def cansum(trgt, ll, memo = {}):
    if trgt in memo:
        return memo[trgt]
    if trgt == 0:
        return []
    if trgt < 0:
        return None
    for i in ll:
        op = trgt - i
        # print(op)
        remainres = cansum(op, ll, memo)
        # print(remainres)
        if remainres is not None:
            remainres.append(i)
            memo[trgt] = remainres
            return memo[trgt]
    return None


sample = [7,2,3,4,7,1]
tar = 300

print(cansum(tar,sample))