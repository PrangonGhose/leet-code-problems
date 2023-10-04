class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        sum = 0
        lst = []
        if s1 == s2:
            return True
        else:
            for i in range(len(s2)):
                if s2[i] != s1[i]:
                    sum += 1
                    lst.append(i)
        if sum == 2:
            if s2[lst[0]] == s1[lst[1]] and s2[lst[1]] == s1[lst[0]]:
                return True
            else: 
                return False
        else:
            return False