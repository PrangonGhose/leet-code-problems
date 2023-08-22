class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        j = -1
        length = len(nums)
        for i in range (length):
            if nums[i] == val:
                while j > -length:
                    if nums[j] != val:
                        nums[i] = nums[j]
                        j -= 1
                        break
                    j -= 1
            else:
                k += 1
        return k