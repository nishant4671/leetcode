class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False

        # required_shifts[x] stores the count of characters in s that need
        # to be shifted by x positions (modulo 26) to match the corresponding
        # character in t. x ranges from 1 to 25.
        # A shift of 0 (s[i] == t[i]) is handled implicitly by not counting it here,
        # as characters that already match or need 0 mod 26 shift don't require
        # a specific move number for conversion. They can simply be "done nothing" to.
        required_shifts = [0] * 26

        for i in range(len(s)):
            if s[i] == t[i]:
                continue # Characters already match, no specific shift move is needed.
            
            # Calculate the minimum positive shift needed to transform s[i] to t[i]
            # This value will be between 1 and 25.
            shift_val = (ord(t[i]) - ord(s[i]) + 26) % 26
            
            # Increment the count for this specific shift value.
            required_shifts[shift_val] += 1
        
        # Now, check if all required shifts can be performed within k moves.
        # For each shift value 'x' (from 1 to 25):
        # If 'count' characters need shift 'x', they must be assigned distinct move numbers.
        # The earliest possible move numbers for achieving a shift of 'x' are:
        # x, x + 26, x + 2*26, ..., x + (count - 1)*26
        # The largest move number required for the 'count'-th instance of shift 'x' is x + (count - 1)*26.
        # This largest move number must not exceed k.
        for x in range(1, 26):
            count = required_shifts[x]
            if count > 0: # If there are characters that need this shift 'x'
                # Calculate the largest move number required for the 'count'-th occurrence of shift 'x'.
                max_move_needed = x + (count - 1) * 26
                
                # If this move number exceeds k, it's impossible to convert.
                if max_move_needed > k:
                    return False
        
        # If all shift requirements can be met, return True.
        return True