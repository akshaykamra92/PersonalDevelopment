str = 'character'
if len(set(str)) == len(str):
    print(str)
else:
    ln = 0
    word = []
    for i in range(len(str)):
        # print(i)
        ip = str[i]
        j = i+1
        while j <= len(str)-1:
            if str[j] not in ip:
                ip += str[j]
            else:
                break
            j += 1
        word.append(ip)
        continue
    print(max(word,key=len))
        # if str[i] not in :
        #     word += str[i]

nums = [0,1]
ll = range(0,max(nums)+1)
print(list(set(nums)^set(ll))[0])

