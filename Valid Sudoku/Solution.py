class Solution(object):
    def isValidSudoku(self, board):
        first_sub = []
        second_sub = []
        third_sub = []
        fourth_sub = []
        fifth_sub = []
        sixth_sub = []
        seventh_sub = []
        eigth_sub = []
        ninth_sub = []
        row = 0
        col = 0
        while row < 9:
            row_checker = []
            if row < 3:
                col = 0
                while col < 9:
                    val = board[row][col]
                    if col < 3 and val != '.':
                        if val not in first_sub and val not in row_checker:
                            first_sub.append(val)
                            row_checker.append(val)
                        else:
                            return False
                    elif col >= 3 and col < 6 and val != '.':
                        if val not in second_sub and val not in row_checker:
                            second_sub.append(val)
                            row_checker.append(val)
                        else:
                            return False
                    elif col >= 6 and col < 9 and val != '.':
                        if val not in third_sub and val not in row_checker:
                            third_sub.append(val)
                            row_checker.append(val)
                        else:
                            return False
                    col += 1
            if row >= 3 and row < 6:
                col = 0
                while col < 9:
                    val = board[row][col]
                    if col < 3 and val != '.':
                        if val not in fourth_sub and val not in row_checker:
                            fourth_sub.append(val)
                            row_checker.append(val)
                        else:
                            return False
                    elif col >= 3 and col < 6 and val != '.':
                        if val not in fifth_sub and val not in row_checker:
                            fifth_sub.append(val)
                            row_checker.append(val)
                        else:
                            return False
                    elif col >= 6 and col < 9 and val != '.':
                        if val not in sixth_sub and val not in row_checker:
                            sixth_sub.append(val)
                            row_checker.append(val)
                        else:
                            return False
                    col += 1
            if row >= 6 and row < 9:
                col = 0
                while col < 9:
                    val = board[row][col]
                    if col < 3 and val != '.':
                        if val not in seventh_sub and val not in row_checker:
                            seventh_sub.append(val)
                            row_checker.append(val)
                        else:
                            return False
                    elif col >= 3 and col < 6 and val != '.':
                        if val not in eigth_sub and val not in row_checker:
                            eigth_sub.append(val)
                            row_checker.append(val)
                        else:
                            return False
                    elif col >= 6 and col < 9 and val != '.':
                        if val not in ninth_sub and val not in row_checker:
                            ninth_sub.append(val)
                            row_checker.append(val)
                        else:
                            return False
                    col += 1
            row += 1
        col = 0
        row = 0
        while col < 9:
            col_checker = []
            row = 0
            while row < 9:
                val = board[row][col]
                if val != '.':
                    if val not in col_checker:
                        col_checker.append(val)
                    else:
                        return False
                row += 1
            col = col + 1
        return True