nums = [17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6]
nums.sort()
counter = 0
val = 0
for i in range(len(nums)):
    # val = nums[i]
    if counter == 2:
        counter = 0
    elif 0 < counter < 2 and val != nums[i]:
        data = val
        counter = 0
        val = nums[i]
        print(data)
    counter += 1
    val = nums[i]


