class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        # 1. Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # If we reached the end of the string or only had whitespace
        if i == n:
            return 0

        # 2. Determine sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        # If we reached the end of the string immediately after sign (e.g., "   -" or "  +")
        if i == n:
            return 0

        # 3. Read digits and convert
        result = 0
        
        # Constants for 32-bit signed integer range
        MAX_INT = 2**31 - 1  # 2147483647
        MIN_INT = -2**31     # -2147483648

        # Pre-calculate parts for overflow checks
        MAX_INT_DIV_10 = MAX_INT // 10  # 214748364
        MAX_INT_MOD_10 = MAX_INT % 10   # 7

        while i < n and s[i].isdigit():
            digit = int(s[i])

            # Check for overflow *before* multiplying and adding the current digit
            # The 'result' is accumulated as a positive number.
            
            # Check for positive overflow (if sign is 1)
            if sign == 1:
                if result > MAX_INT_DIV_10 or (result == MAX_INT_DIV_10 and digit > MAX_INT_MOD_10):
                    return MAX_INT
            # Check for negative overflow (if sign is -1)
            else: # sign == -1
                # The absolute value of MIN_INT (2^31) is MAX_INT + 1.
                # So for negative numbers, the threshold for the last digit
                # is MAX_INT_MOD_10 + 1 (which is 8).
                if result > MAX_INT_DIV_10 or (result == MAX_INT_DIV_10 and digit > (MAX_INT_MOD_10 + 1)):
                    return MIN_INT

            result = result * 10 + digit
            i += 1
            
        # 4. Apply sign and return
        return sign * result