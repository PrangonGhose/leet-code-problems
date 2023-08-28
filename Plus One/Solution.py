class Solution(object):
    def plusOne(self, digits):
        string = ''
        output = []
        for i in digits:
            string += str(i)
        string = int(string) 
        string += 1
        string = str(string)
        for i in string:
            output.append(int(i))
        return output