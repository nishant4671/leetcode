from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        # Flags to remember if the first row or first column originally contained a zero.
        # This is crucial because we'll use the first row and first column themselves
        # as markers for other rows and columns.
        first_row_has_zero = False
        first_col_has_zero = False

        # Step 1: Determine if the first row needs to be zeroed.
        # Iterate through the first row to check for any zeros.
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break
        
        # Step 2: Determine if the first column needs to be zeroed.
        # Iterate through the first column to check for any zeros.
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break

        # Step 3: Use the first row and first column as markers for the rest of the matrix.
        # Iterate through the matrix starting from (1,1) to (m-1, n-1).
        # If an element matrix[i][j] (where i > 0 and j > 0) is 0,
        # set its corresponding marker in the first row (matrix[0][j]) and first column (matrix[i][0]) to 0.
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark row i
                    matrix[0][j] = 0  # Mark column j
        
        # Step 4: Zero out the "inner" part of the matrix based on the markers.
        # Iterate from (1,1) to (m-1, n-1).
        # If matrix[i][0] is 0 (meaning row i needs to be zeroed) OR
        # if matrix[0][j] is 0 (meaning column j needs to be zeroed),
        # then set matrix[i][j] to 0.
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Step 5: Zero out the first row if it originally contained a zero.
        # This step must be performed *after* setting zeros for the inner matrix,
        # otherwise, the `matrix[0][j]` markers used in Step 4 could be overwritten prematurely.
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Step 6: Zero out the first column if it originally contained a zero.
        # This step must also be performed *after* setting zeros for the inner matrix.
        # It's important to do this after zeroing the first row (if applicable) 
        # or at least in a way that doesn't conflict with its markers.
        # In this specific order, it doesn't conflict with matrix[0][j] markers for j>0
        # as those are handled by `first_row_has_zero`.
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0