class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if (nums[i] == nums[i + 1]) :
                return 1
            else:
                pass
        return 0