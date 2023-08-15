class Solution(object):
    def romanToInt(self, s):
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C': 100, 'D': 500, 'M': 1000}
        integer = 0
        i = 0
        l = len(s)
        while i < l-1:
            num1 = dict[s[i]]
            num2 = dict[s[i+1]]
            if num1 > num2 or num1 == num2:
                integer += num1
                i += 1
            else:
                integer += (num2-num1)
                i += 2
        if i != l:
            return integer + dict[s[-1]]
        else:
            return integer