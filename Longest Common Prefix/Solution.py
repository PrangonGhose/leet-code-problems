class Solution(object):
    def longestCommonPrefix(self, strs):
        lowest_len = len(strs[0])
        lowest_len_word = strs[0]
        output = ''
        for i in range(len(strs)):
            if len(strs[i]) < lowest_len:
                lowest_len = len(strs[i])
                lowest_len_word = strs[i]
        for i in range (lowest_len):
            for j in range(len(strs)):
                if lowest_len_word[i] != strs[j][i]:
                    return output
            output += lowest_len_word[i]
        return output