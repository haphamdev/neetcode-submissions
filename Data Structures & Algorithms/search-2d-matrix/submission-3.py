class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]: return False
        top, bottom = 0, len(matrix) -1

        while top < bottom - 1:
            m = (top + bottom) // 2
            if matrix[m][0] <= target:
                top = m
            else:
                bottom = m

        rowIndex = bottom if matrix[bottom][0] <= target else top
        row = matrix[rowIndex]
        l,r = 0, len(row) - 1

        print(row)
        while l <= r:
            m = (l + r) // 2
            if row[m] == target: return True
            if row[m] < target:
                l = m + 1
            else:
                r = m - 1
        return False