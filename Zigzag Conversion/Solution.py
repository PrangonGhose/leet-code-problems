class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row = 1
        col = 1
        state = "forward"
        result = {}
        output = ''
        if numRows == 1:
            output = s
        else:
            for i in range(len(s)):
                if row == 1 and state == 'reverse':
                    result[str(row),str(col)] = s[i]
                    row += 1
                    state = 'forward'
                elif row < numRows and state == 'forward':
                    result[str(row),str(col)] = s[i]
                    row += 1
                elif row < numRows and state == 'reverse':
                    result[str(row),str(col)] = s[i]
                    row -= 1
                    if i < len(s) - 1:
                        col += 1
                elif row == numRows:
                    result[str(row),str(col)] = s[i]
                    row -= 1
                    if i < len(s) - 1:
                        col += 1
                    state = 'reverse'

            for i in range(numRows):
                for j in range(col):
                    r = (str(i+1),str(j+1))
                    try:
                        output += result[r]
                    except KeyError:
                        pass
    
        return output