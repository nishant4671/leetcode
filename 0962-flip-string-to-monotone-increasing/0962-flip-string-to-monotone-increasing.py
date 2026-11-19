class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # dp0: minimum flips to make the prefix s[0...i] entirely zeros.
        # dp1: minimum flips to make the prefix s[0...i] monotone increasing and ending with one.
        
        # Base cases for an empty prefix (before s[0]):
        # No flips needed to make it all zeros or all ones (empty string is monotone).
        dp0 = 0 
        dp1 = 0

        for char in s:
            # Store dp0 from the previous iteration, as it will be updated for the current iteration
            # but is also needed for the dp1 calculation for the current iteration.
            prev_dp0 = dp0 
            
            # Calculate new dp0 (cost to make current prefix all '0's)
            # If current char is '0', no flip needed: cost is previous dp0.
            # If current char is '1', it must be flipped to '0': cost is previous dp0 + 1.
            dp0 = prev_dp0 + (1 if char == '1' else 0)
            
            # Calculate new dp1 (cost to make current prefix monotone and ending with '1')
            # If current char is '0', it must be flipped to '1': cost is +1.
            # If current char is '1', no flip needed: cost is +0.
            # The previous prefix s[0...i-1] could have ended with '0' (prev_dp0)
            # or already monotone ending with '1' (dp1). We take the minimum path.
            dp1 = min(prev_dp0, dp1) + (1 if char == '0' else 0)

        # After iterating through the entire string, 
        # the minimum flips is either to make the entire string all zeros (dp0),
        # or to make it monotone increasing and ending with one (dp1).
        return min(dp0, dp1)