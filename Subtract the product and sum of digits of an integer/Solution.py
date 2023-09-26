class Solution:
  def subtractProductAndSum(self, n: int) -> int:
    n = str(n)
    sum = 0
    mul = 1
    for i in n:
      sum += int(i)
      mul = mul*int(i)
    return (-sum+mul)