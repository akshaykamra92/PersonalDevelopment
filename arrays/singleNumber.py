i =0
nums=[4,2,1,2,3,4,3,1,5]
nums.sort()
while i <= len(nums)-1:
    if(i == len(nums)-1):
        print(nums[i])
        break
    else:
        if nums[i]!=nums[i+1]:
            print(nums[i])
            break
        else:
            i +=2