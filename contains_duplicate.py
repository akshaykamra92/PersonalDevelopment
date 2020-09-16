
def containsDuplicate(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if (nums[i] == nums[i + 1]) :
            return 1
        else:
            pass
    return 0
nums = [1,2,3,1]
print(containsDuplicate(nums))

