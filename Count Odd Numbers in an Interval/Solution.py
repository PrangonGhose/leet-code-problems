class Solution:
  def countOdds(self, low: int, high: int) -> int:
    if low%2 != 0 and high%2 != 0:
      j = (high - low)/2 + 1
    elif low%2 != 0 and high%2 == 0:
      j = (high - (low-1))/2
    elif low%2 == 0 and high%2 != 0:
      j = ((high+1) - low)/2
    elif low%2 ==0 and high%2 == 0:
      j = (high - low)/2
    return int(j)