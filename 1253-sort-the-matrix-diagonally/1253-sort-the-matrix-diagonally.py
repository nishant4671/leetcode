import collections

class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])

        diagonals = collections.defaultdict(list)

        for r in range(m):
            for c in range(n):
                diagonals[r - c].append(mat[r][c])

        for diff in diagonals:
            diagonals[diff].sort()
        
        for diff in diagonals:
            diagonals[diff] = iter(diagonals[diff])

        for r in range(m):
            for c in range(n):
                mat[r][c] = next(diagonals[r - c])

        return mat