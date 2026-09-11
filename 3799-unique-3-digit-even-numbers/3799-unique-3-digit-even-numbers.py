import itertools
from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        valid_numbers = set()
        n = len(digits)
        
        # Iterate over all unique permutations of three distinct indices
        # from the 'digits' array. This implicitly ensures that each copy of a digit
        # is used at most once per number, as distinct indices refer to distinct copies.
        for i, j, k in itertools.permutations(range(n), 3):
            d1 = digits[i]
            d2 = digits[j]
            d3 = digits[k]
            
            # Condition 1: The first digit (hundreds place) cannot be 0
            if d1 == 0:
                continue
            
            # Condition 2: The number must be even, so the last digit (units place) must be even
            if d3 % 2 != 0:
                continue
            
            # Form the three-digit number
            num = d1 * 100 + d2 * 10 + d3
            
            # Add the number to a set to count only distinct numbers
            valid_numbers.add(num)
            
        return len(valid_numbers)