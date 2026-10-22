class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] != matrix[r-1][c-1]:
                    return False
        
        return True