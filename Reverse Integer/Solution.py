class Solution:
  def reverse(self, x: int) -> int:
    s = str(x)
    if s[0] != '-':
      s = s[::-1]
      result = int(s)
    else:
      rest = s[1::]
      rest = rest[::-1]
      result = int(rest) * -1
    if result < -2**31 or result > 2**31 - 1:
      return 0
    else:
      return result