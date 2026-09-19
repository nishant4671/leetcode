class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # Initialize an empty list to store all rows of Pascal's triangle.
        triangle = []

        # Iterate through each row index from 0 up to numRows - 1.
        for i in range(numRows):
            # Each row 'i' (0-indexed) will have 'i + 1' elements.
            # Initialize the current row with zeros.
            current_row = [0] * (i + 1)

            # The first element of every row in Pascal's triangle is always 1.
            current_row[0] = 1
            
            # The last element of every row (except the very first row) is also 1.
            # For i=0, current_row[0] is the only element, so this condition implicitly handles it.
            if i > 0:
                current_row[i] = 1

            # Calculate the intermediate elements for the current row.
            # Intermediate elements exist for rows with length greater than 2 (i.e., i > 1).
            # The value of an element is the sum of the two elements directly above it
            # in the previous row.
            if i > 1:
                # Get the previous row from the 'triangle' list.
                previous_row = triangle[i - 1]

                # Iterate from the second element (index 1) up to (but not including) the last element.
                for j in range(1, i):
                    current_row[j] = previous_row[j - 1] + previous_row[j]
            
            # Add the newly generated current row to our triangle.
            triangle.append(current_row)
        
        # Return the complete Pascal's triangle.
        return triangle