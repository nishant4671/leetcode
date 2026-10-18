class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Iterate from the rightmost digit to the leftmost digit.
        # The goal is to find the rightmost occurrence of an odd digit.
        # Once found, the substring starting from the beginning of 'num'
        # up to and including this odd digit will be the largest odd number.
        # This is because:
        # 1. It maximizes the length of the number (longer numbers are generally larger).
        # 2. It ensures the number starts from the earliest possible position (index 0),
        #    contributing to a larger value compared to substrings starting later.
        
        n = len(num)
        for i in range(n - 1, -1, -1):
            # Check if the current digit num[i] is odd.
            # We can directly check if the character is one of '1', '3', '5', '7', '9'.
            if num[i] in {'1', '3', '5', '7', '9'}:
                # If an odd digit is found at index 'i',
                # the substring from index 0 up to and including index 'i'
                # (i.e., num[0...i]) is the largest odd number.
                # Python's slice `num[:i+1]` correctly extracts this substring.
                return num[:i+1]
        
        # If the loop completes without finding any odd digit,
        # it means there are no odd digits in the entire string 'num'.
        # Therefore, no odd number substring exists.
        return ""