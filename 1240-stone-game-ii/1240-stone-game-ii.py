class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        N = len(piles)

        # Precompute suffix sums for efficiency.
        # suffix_sum[i] stores the sum of piles from index i to N-1.
        # suffix_sum[N] will be 0, representing no piles left.
        suffix_sum = [0] * (N + 1)
        for i in range(N - 1, -1, -1):
            suffix_sum[i] = piles[i] + suffix_sum[i+1]

        # Memoization table: memo[i][m] stores the maximum stones the current
        # player can get starting from piles[i:] with the current M value m.
        # Initialize with -1 to indicate uncomputed states.
        # i ranges from 0 to N. m ranges from 1 to N (the maximum possible M value).
        memo = [[-1] * (N + 1) for _ in range(N + 1)]

        # dp function: calculates the maximum stones the current player can get
        # starting from piles[i:] with the current M value m.
        def dp(i, m):
            # Base case: If no piles left, the current player gets 0 stones.
            if i == N:
                return 0
            
            # If this state has already been computed, return the stored result.
            if memo[i][m] != -1:
                return memo[i][m]

            max_stones_for_current_player = -1
            current_piles_taken_sum = 0  # Sum of stones taken in the current move (X piles)

            # The current player can take X piles, where 1 <= X <= 2*M.
            for X in range(1, 2 * m + 1):
                # If taking X piles would exceed the remaining piles, stop.
                # All remaining piles would have been taken by now.
                if i + X > N:
                    break
                
                # Add the stones of the current X-th pile to the sum for this move.
                current_piles_taken_sum += piles[i + X - 1]
                
                # Update M for the next turn: M becomes max(old M, X).
                new_m = max(m, X)

                # Recursively calculate the maximum stones the *next* player would get
                # from the remaining piles, starting at index i + X with the new_m.
                stones_next_player_gets = dp(i + X, new_m)

                # The total stones available from index i + X to N-1 (inclusive).
                total_remaining_stones_from_next_start = suffix_sum[i + X]

                # The current player's score for this specific choice of X piles:
                # It's the stones taken in this move (current_piles_taken_sum)
                # PLUS the stones the current player ultimately gets from the subsequent
                # portion of the game (total_remaining_stones_from_next_start minus
                # what the next player optimally takes from that portion).
                stones_this_turn = current_piles_taken_sum + \
                                   (total_remaining_stones_from_next_start - stones_next_player_gets)
                
                # Update the maximum stones the current player can get for this state (i, m).
                max_stones_for_current_player = max(max_stones_for_current_player, stones_this_turn)
            
            # Store the computed result in the memoization table and return it.
            memo[i][m] = max_stones_for_current_player
            return max_stones_for_current_player

        # Alice starts first at index 0 with M = 1.
        return dp(0, 1)