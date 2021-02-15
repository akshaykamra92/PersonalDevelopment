def sockMerchant(n, ar):
    ar.sort()
    i = 0
    print("test")
    while i <= (n-1):
        if len(ar) == 1:
            break
        if ar[i] == ar[i + 1]:
            ar.pop(i+1)
            ar.pop(i)
        else :
            i+= 1
        print(ar)
    res = len(ar)
    print(res)
    return res



n = 7

ar = [1,2,2,2,1,3,1]

result = sockMerchant(n, ar)
print("result",result)