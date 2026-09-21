class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        
        # Initialize the count of ones in the right substring.
        # Initially, the entire string is considered the "right" part before any split.
        ones_right = s.count('1')
        
        # Initialize the count of zeros in the left substring.
        # Initially, the "left" part is empty.
        zeros_left = 0
        
        # Initialize max_score. Since the minimum possible score is 1 (e.g., "00" split "0"|"0" gives 1+0=1),
        # 0 is a safe initial value.
        max_score = 0
        
        # Iterate through all possible split points.
        # A split occurs after index `i`.
        # The left substring will be s[0...i].
        # The right substring will be s[i+1...n-1].
        # Both substrings must be non-empty.
        # This means `i` can range from 0 (left = s[0], right = s[1...n-1])
        # up to n-2 (left = s[0...n-2], right = s[n-1]).
        for i in range(n - 1):
            # When we move the split point one character to the right (i.e., s[i] moves from right to left),
            # we update our counts.
            if s[i] == '0':
                zeros_left += 1
            else:  # s[i] == '1'
                ones_right -= 1
            
            # Calculate the current score for this split.
            current_score = zeros_left + ones_right
            
            # Update the maximum score found so far.
            if current_score > max_score:
                max_score = current_score
                
        return max_score