class Solution(object):
    def lengthOfLastWord(self, s):
        output = ''
        for i in reversed(range(len(s))):
            if s[i] != ' ':
                output += s[i]
            else:
                if output:
                    return len(output)
        return len(output)