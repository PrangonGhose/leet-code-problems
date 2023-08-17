class Solution:
    def signFunc(self, mul: int) -> int:
        if mul > 0:
            return 1
        elif mul < 0:
            return -1
        else:
            return 0
        
    def arraySign(self, nums: List[int]) -> int:
        mul = 1
        for i in nums:
            mul = mul*i
        x = self.signFunc(mul)
        return x