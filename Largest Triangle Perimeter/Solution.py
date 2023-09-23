class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1,-1,-1):
            a = nums[i]
            b = nums[i-1]
            c = nums[i-2]
            if a >= b and a >= c and b+c > a:
                return a+b+c
        return 0