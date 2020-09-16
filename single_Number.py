
def singleNumber(list):
    i = 0
    nums.sort()
    while i < (len(nums)):
        if len(nums) == 1:
            return nums[0]
        elif (nums[i] == nums[i + 1]):
            nums.pop(i + 1)
            nums.pop(i)
        else:
            i += 1
    return nums[0]

nums = [4,1,2,1,2]
print(singleNumber(nums))
