class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> list[int]:
        stones = sorted([a, b, c])
        x, y, z = stones[0], stones[1], stones[2]

        # Calculate minimum moves
        min_moves = 0
        if z - x == 2:
            # Stones are already in consecutive positions (e.g., 2, 3, 4)
            min_moves = 0
        elif (y - x <= 2) or (z - y <= 2):
            # One of the gaps is 1 or 2. This means we can make the stones
            # consecutive in a single move.
            # Example cases:
            # 1. (1, 2, 5): y-x = 1. Move 5 to 3. Result (1, 2, 3). (1 move)
            # 2. (1, 4, 5): z-y = 1. Move 1 to 3. Result (3, 4, 5). (1 move)
            # 3. (1, 3, 7): y-x = 2. Move 7 to 2. Result (1, 2, 3). (1 move)
            # 4. (1, 5, 7): z-y = 2. Move 1 to 6. Result (5, 6, 7). (1 move)
            min_moves = 1
        else:
            # Both gaps are greater than 2 (y-x > 2 and z-y > 2).
            # This requires exactly 2 moves.
            # Example: (1, 5, 10)
            # First move: Move 1 to 4 (y-1). Stones become (4, 5, 10). (1 move)
            # Now, the situation is (X, X+1, Z_far). This can be solved in 1 more move
            # by moving 10 to 6. Total 2 moves.
            min_moves = 2
        
        # Calculate maximum moves
        # Each move picks an endpoint stone and moves it into an empty slot
        # between the current endpoints. This effectively fills one empty slot
        # between the current lowest and highest stones.
        # The total number of empty slots that need to be filled to make the stones
        # consecutive is the sum of empty slots between x and y, and y and z.
        # Empty slots between x and y = (y - x - 1)
        # Empty slots between y and z = (z - y - 1)
        # Total empty slots = (y - x - 1) + (z - y - 1)
        # This simplifies to z - x - 2.
        max_moves = (y - x - 1) + (z - y - 1)

        return [min_moves, max_moves]