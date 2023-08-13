class Solution:
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            diff = target - nums[i]
            if diff in nums and i != nums.index(diff):
                return [i,nums.index(diff)]