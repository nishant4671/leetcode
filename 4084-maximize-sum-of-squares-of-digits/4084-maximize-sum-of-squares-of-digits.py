class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # Initial constraint check:
        # A number with 'num' digits can have a minimum sum of 1 (e.g., 10...0)
        # and a maximum sum of 9 * num (e.g., 99...9).
        # Since 'sum' is guaranteed to be positive (sum >= 1), we only need to check the upper bound.
        if sum > 9 * num:
            return ""

        max_score = -1
        result_n_str = ""

        # The core idea is that to maximize the sum of squares of digits for a fixed total sum,
        # the digits should be as extreme as possible (i.e., concentrated towards 0s and 9s).
        # This implies that an optimal set of digits will contain:
        # - some number of 9s
        # - some number of 0s
        # - at most one digit 'r' in the range [1, 8]
        # We iterate through possible values for this single digit 'r' (from 0 to 8).
        # 'r = 0' signifies that all non-zero digits must be 9s.
        # 'r > 0' signifies that there is exactly one digit 'r' (1-8), and the rest are 0s or 9s.
        for r in range(9):
            # Calculate the sum that needs to be formed by 9s and 0s, after accounting for 'r'.
            current_sum_for_9s = sum - r

            # If current_sum_for_9s is negative, it means 'r' alone is larger than 'sum',
            # so this 'r' cannot be part of the sum.
            if current_sum_for_9s < 0:
                continue
            
            # The remaining sum (current_sum_for_9s) must be perfectly divisible by 9,
            # as it needs to be formed exclusively by 9s and 0s.
            if current_sum_for_9s % 9 != 0:
                continue

            num_9s = current_sum_for_9s // 9
            
            # The total number of digits is 'num'. We've used 'num_9s' for 9s and
            # 1 digit for 'r' (if r > 0). The rest must be 0s.
            num_zeros = num - num_9s - (1 if r > 0 else 0)

            # Check if the calculated number of 9s and 0s are valid (non-negative).
            # If num_9s is too large for the available 'num' digits, num_zeros would be negative.
            if num_9s < 0 or num_zeros < 0:
                continue
            
            # The first digit of the number 'n' must be non-zero.
            # When we construct the number string by sorting digits in descending order,
            # the first digit will naturally be the largest non-zero digit available.
            # Since 'sum' is positive, there will always be at least one non-zero digit
            # (either 'r' or one of the 9s), so this condition is implicitly met for any valid construction.

            current_score = num_9s * 81 + r * r # Calculate score: sum of squares

            # Construct the list of digits for the current candidate, then convert to string.
            # This is done efficiently using list multiplication and extend.
            digits_list = [9] * num_9s
            if r > 0:
                digits_list.append(r)
            digits_list.extend([0] * num_zeros)
            
            # Sort digits in descending order to form the numerically largest integer
            # (which is required for tie-breaking by the problem statement).
            candidate_n_str = "".join(map(str, sorted(digits_list, reverse=True)))

            # Update max_score and result_n_str if current candidate is better.
            if current_score > max_score:
                max_score = current_score
                result_n_str = candidate_n_str
            elif current_score == max_score:
                # If scores are equal, choose the numerically larger integer.
                if candidate_n_str > result_n_str:
                    result_n_str = candidate_n_str
        
        return result_n_str