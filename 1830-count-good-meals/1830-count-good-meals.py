class Solution:
    def countPairs(self, deliciousness: list[int]) -> int:
        MOD = 10**9 + 7
        
        # The maximum possible deliciousness value is 2^20.
        # The maximum possible sum of two deliciousness values is 2^20 + 2^20 = 2 * 2^20 = 2^21.
        # The powers of two we need to consider for sums range from 2^0 (1) up to 2^21.
        # We precompute these powers for efficient lookup.
        # There are 22 such powers (from 2^0 to 2^21).
        powers_of_two = [1 << i for i in range(22)]
        
        # A hash map to store the frequency of each deliciousness value encountered so far.
        freq_map = {}
        
        # Initialize the count of good meals.
        good_meals_count = 0
        
        # Iterate through each deliciousness value in the input list.
        for d in deliciousness:
            # For the current deliciousness 'd', we try to find a 'complement'
            # such that 'd + complement' equals a power of two.
            # We iterate through all relevant precomputed powers of two.
            for power_of_two in powers_of_two:
                complement = power_of_two - d
                
                # If the complement is found in our frequency map, it means we have
                # previously encountered 'freq_map[complement]' items that, when
                # paired with the current 'd', form a sum equal to 'power_of_two'.
                # We add this count to our total. The modulo operation is applied
                # at each addition to prevent integer overflow for large counts.
                if complement in freq_map:
                    good_meals_count = (good_meals_count + freq_map[complement]) % MOD
            
            # After checking for complements with previously seen items,
            # add the current deliciousness value 'd' to our frequency map.
            # This makes 'd' available for future items in the 'deliciousness' list
            # to form pairs with.
            freq_map[d] = freq_map.get(d, 0) + 1
            
        return good_meals_count