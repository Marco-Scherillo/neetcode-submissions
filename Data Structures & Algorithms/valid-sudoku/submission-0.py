class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #get box: (row / 3) * 3 + (col / 3)
        seen_row = defaultdict(set)
        seen_col = defaultdict(set)
        seen_box = defaultdict(set)
        n = len(board)
        m = len(board[0])

        for i in range(n):
            for j in range(m):
                cell = board[i][j]
                if cell == '.':
                    continue
                box = (i // 3) * 3 + (j // 3)
                #already seen return false
                if cell in seen_row[i] or cell in seen_col[j] or cell in seen_box[box]:
                    return False
                #not seen yet
                seen_row[i].add(cell)
                seen_col[j].add(cell)
                seen_box[box].add(cell)
        return True
                

