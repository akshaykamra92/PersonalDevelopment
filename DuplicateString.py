nums = [1, 2, 1, 3, 4]
# values.sort()

# print(len(set(values)) != len(values))


duplicates = {}
val = 0
for i in range(len(nums)):
    if nums[i] in duplicates:
        val = 1
        break
    else:
        duplicates[nums[i]] = 1
