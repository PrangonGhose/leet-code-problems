class Solution(object):
    def topKFrequent(self, nums, k):
        new_dict = {}
        result = []
        for i in nums:
            if i not in new_dict:
                new_dict[i] = 1
            else:
                new_dict[i] += 1
        val = list(new_dict.values())
        val.sort()
        while k != 0:
            for i in new_dict:
                if new_dict[i] == val[-1] and i not in result:
                    result.append(i)
                    val.pop()
                    break
            k -= 1
        return result