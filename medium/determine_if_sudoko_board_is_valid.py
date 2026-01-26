# from typing import List

class Solution:
    def isValidSudoku(self, board):  
        # 9 sets for rows, cols, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                # Skip empty cells
                if val == ".":
                    continue

                # Find box index (0 to 8)
                box_index = (r // 3) * 3 + (c // 3)

                # If duplicate found -> invalid
                if (val in rows[r]) or (val in cols[c]) or (val in boxes[box_index]):
                    return False

                # Otherwise mark it as seen
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)

        return True




# self refers to the current object (instance) of the class Solution


# 6) board

# This is the actual input data you are solving on.


#  rows = [set() for _ in range(9)]        in here the sqaure bracket sayd e are initializing a list , each list contains 9 sets , 9 rows , 9 colums and 9 boxes 

#         cols = [set() for _ in range(9)]
#         boxes = [set() for _ in range(9)]



