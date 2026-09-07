class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        
        # dp[i] stores the number of distinct non-empty subsequences ending with the i-th lowercase letter.
        # For example, dp[0] for 'a', dp[1] for 'b', ..., dp[25] for 'z'.
        dp = [0] * 26
        
        # total_sum stores the total number of distinct non-empty subsequences found so far.
        total_sum = 0
        
        for char_s in s:
            char_code = ord(char_s) - ord('a')
            
            # Calculate the number of distinct subsequences that can be formed ending with char_s
            # using the string processed up to the current character.
            # This count includes:
            # 1. The character char_s itself (as a single-character subsequence).
            # 2. char_s appended to every distinct non-empty subsequence found so far (total_sum).
            current_new_for_char = (1 + total_sum) % MOD
            
            # Retrieve the count of distinct subsequences that ended with char_s
            # before processing the current char_s. These are the subsequences
            # that would be double-counted if we simply added current_new_for_char
            # to total_sum without adjustment.
            prev_count_for_char = dp[char_code]
            
            # Update total_sum:
            # We add all the new subsequences ending with char_s (current_new_for_char).
            # Then, we subtract the count of subsequences that ended with an earlier
            # instance of char_s (prev_count_for_char) to avoid double-counting.
            # The '+ MOD' before the final '% MOD' handles cases where the subtraction
            # results in a negative number.
            total_sum = (total_sum + current_new_for_char - prev_count_for_char + MOD) % MOD
            
            # Update the dp array for char_s with its new total count of distinct
            # subsequences ending with it.
            dp[char_code] = current_new_for_char
            
        return total_sum