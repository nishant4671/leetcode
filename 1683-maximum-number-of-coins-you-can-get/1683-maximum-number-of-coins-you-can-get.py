class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        
        my_total_coins = 0
        
        # The total number of piles is 3n. We form n triplets.
        # In each triplet (x, y, z) where x < y < z,
        # Alice takes z (maximum), I take y (middle), Bob takes x (minimum).
        # To maximize my total coins, I must maximize the sum of y's I pick.
        #
        # By sorting the piles in ascending order, we have:
        # s_0, s_1, ..., s_{3n-1}
        # where s_0 <= s_1 <= ... <= s_{3n-1}.
        #
        # To maximize my 'y' pick in each round, I should aim for the largest possible 'y'
        # from the remaining piles. This means pairing the largest available pile (for Alice)
        # with the second largest available pile (for me) and the smallest available pile (for Bob).
        # This strategy ensures Bob removes the least valuable pile, leaving more valuable
        # piles for Alice and me to contest.
        #
        # Following this greedy strategy:
        # 1. In the first round, we consider (piles[0], piles[len-2], piles[len-1]).
        #    Alice takes piles[len-1], I take piles[len-2], Bob takes piles[0].
        # 2. In the second round, we consider (piles[1], piles[len-4], piles[len-3]).
        #    Alice takes piles[len-3], I take piles[len-4], Bob takes piles[1].
        # This pattern continues.
        #
        # The piles I get are:
        # piles[len-2], piles[len-4], piles[len-6], ..., up to piles[len/3].
        # The loop needs to run `len(piles) // 3` times.
        
        num_triplets = len(piles) // 3
        
        # `my_current_pick_idx` starts at the index of the largest pile I can take in the first round.
        # This is `len(piles) - 2` (the second-to-last element in the sorted array).
        my_current_pick_idx = len(piles) - 2
        
        # Iterate `num_triplets` times to collect my share from each round.
        for _ in range(num_triplets):
            my_total_coins += piles[my_current_pick_idx]
            
            # After picking my pile (e.g., piles[i]) and Alice picking piles[i+1],
            # the next largest pile available for me will be two positions to the left
            # in the sorted array (piles[i-2]).
            my_current_pick_idx -= 2
            
        return my_total_coins