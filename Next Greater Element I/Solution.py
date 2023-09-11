class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst = []
        for i in nums1:
            key = 0
            j = nums2.index(i)
            for k in range(j,len(nums2)):
                if nums2[k] > nums2[j]:
                    lst.append(nums2[k])
                    key = 1
                    break
            if key == 0:
                lst.append(-1)
        return lst