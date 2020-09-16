
data = [1,2,3,4]
nums = [1,2,3,1]
val = 0
nums.sort()
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]!=nums[j]:
            break
        else:
            val =1
            break
    if val > 0:
        break
print(val)
