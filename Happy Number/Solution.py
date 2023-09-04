class Solution:
    def square(self, n):
        m = str(n)
        sum = 0
        for i in m:
            sum = int(i)**2 + sum
        return sum
        
    def isHappy(self, n: int) -> bool:
        result = n
        lst = []
        while(True):
            result = self.square(result)
            if result == 1:
                return True
            elif result in lst:
                return False
            else:
                lst.append(result)