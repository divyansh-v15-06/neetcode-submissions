class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        squares=[set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                num=board[r][c]
                box=(r//3)*3+ (c//3)
                if num in rows[r]: return False 
                if num in col[c]:return False
                if num in squares[box]:return False 
                rows[r].add(num)
                col[c].add(num)
                squares[box].add(num)
        return True        
