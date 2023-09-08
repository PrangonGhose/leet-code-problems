# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        start = 1
        end = n
        while start < end:
            check = (start + end) // 2
            status = isBadVersion(check)
            if status == True:
                end = check
            else:
                start = check + 1
        return start