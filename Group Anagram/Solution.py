class Solution(object):
    def groupAnagrams(self, strs):
        temp = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in temp:
                temp[sortedWord] = [word]
            else:
                temp[sortedWord].append(word)
        anagrams = []
        for values in temp.values():
            anagrams.append(values)
        return anagrams