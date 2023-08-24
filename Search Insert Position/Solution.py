class Solution(object):
    def searchInsert(self, nums, target):
        start_ind = 0
        end_ind = len(nums) - 1
        index_to_check = (start_ind + end_ind) // 2
        num_to_check = nums[index_to_check]
        while start_ind < end_ind:
            index_to_check = (start_ind + end_ind) // 2
            num_to_check = nums[index_to_check]
            if num_to_check < target:
                start_ind = index_to_check + 1
            elif num_to_check > target:
                end_ind = index_to_check - 1
            else:
                start_ind = index_to_check
                end_ind = index_to_check
        if start_ind == end_ind:
            num_to_check = nums[start_ind]
            if num_to_check >= target:
                return start_ind
            else:
                return start_ind+1
        else:
            return start_ind