class Solution(object):
    def isValidSudoku(self, board):
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                char = board[i][j]
                if char == '.':
                    continue

                else:
                    if char not in row[i]:
                        row[i].add(char)
                    else:
                        return False
                    if char not in col[j]:
                        col[j].add(char)
                    else:
                        return False
                    idx = (i // 3)*3 + (j // 3)
                    if char not in box[idx]:
                        box[idx].add(char)
                    else:
                        return False

        return True
