class Solution(object):
    def strStr(self, haystack, needle):
        output = -1
        hayLen = len(haystack)
        needLen = len(needle)
        if hayLen < needLen:
            return output
        for i in range (hayLen):
            if haystack[i] == needle[0]:
                match = True
                j = 0
                while i+j < hayLen and j < needLen:
                    if haystack[i+j] != needle[j]:
                        match = False
                        break
                    j += 1
                if match == True and hayLen - i >= needLen:
                    output = i
                    break
        return output