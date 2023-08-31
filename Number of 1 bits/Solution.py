class Solution:
    def hammingWeight(self, n: int) -> int:
        n = str(bin(n)).replace("0b","")
        sum = 0
        for i in n:
            if i == '1':
                sum += 1
        return sum