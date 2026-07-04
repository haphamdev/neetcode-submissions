class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = [[set() for _ in range(3)] for _ in range(3)]
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                n = board[r][c]
                if n == '.': continue
                if n in squares[r//3][c//3] or n in rows[r] or n in cols[c]: 
                    return False
                squares[r//3][c//3].add(n)
                rows[r].add(n)
                cols[c].add(n)
            
        return True