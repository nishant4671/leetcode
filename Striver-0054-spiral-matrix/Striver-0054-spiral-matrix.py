class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # Handle empty matrix case.
        # Constraints (1 <= m, n) imply matrix is never empty, but good practice.
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        result = []

        # Initialize boundary pointers
        top, bottom = 0, m - 1
        left, right = 0, n - 1

        # Loop until boundaries cross each other
        while top <= bottom and left <= right:
            # 1. Traverse Right: from left to right along the current top row
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1 # Move top boundary down to exclude the row just traversed

            # 2. Traverse Down: from top to bottom along the current right column
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1 # Move right boundary left to exclude the column just traversed

            # 3. Traverse Left: from right to left along the current bottom row
            # This step only executes if there's still a valid row to traverse
            # (i.e., top hasn't crossed bottom yet). This is crucial for matrices
            # like [[1,2,3]] where 'top' might become greater than 'bottom'
            # after step 1, meaning there's no distinct bottom row left.
            if top <= bottom:
                for col in range(right, left - 1, -1): # Iterate backwards
                    result.append(matrix[bottom][col])
                bottom -= 1 # Move bottom boundary up to exclude the row just traversed

            # 4. Traverse Up: from bottom to top along the current left column
            # This step only executes if there's still a valid column to traverse
            # (i.e., left hasn't crossed right yet). This is crucial for matrices
            # like [[1],[2],[3]] where 'right' might become less than 'left'
            # after step 2, meaning there's no distinct left column left.
            if left <= right:
                for row in range(bottom, top - 1, -1): # Iterate backwards
                    result.append(matrix[row][left])
                left += 1 # Move left boundary right to exclude the column just traversed
        
        return result