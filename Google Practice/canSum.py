def cansum(trgt, ll):
    if trgt == 0:
        return True
    if trgt < 0:
        return False
    for i in ll:
        op = trgt - i
        if cansum(op, ll) is True:
            return True
    return False


sample = [7]
tar = 7

print(cansum(tar,sample))