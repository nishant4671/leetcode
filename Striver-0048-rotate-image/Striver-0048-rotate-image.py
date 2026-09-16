class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Step 1: Transpose the matrix
        # Swap matrix[i][j] with matrix[j][i]
        # We iterate over the upper triangle (including diagonal) to avoid double-swapping elements.
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row of the transposed matrix
        # This completes the 90-degree clockwise rotation.
        for i in range(n):
            matrix[i].reverse()