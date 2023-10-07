class Solution(object):
  def containsDuplicate(self, nums):
    new_array = set()
    for i in nums:
      if i in new_array:
        return True
      else:
        new_array.add(i)