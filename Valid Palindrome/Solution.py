import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        letters_only = re.sub(r"[^a-zA-Z0-9]", "", s)
        letters_only = letters_only.lower()
        for i in range (len(letters_only)):
            if letters_only[i] != letters_only[-1-i]:
                return False
        return True