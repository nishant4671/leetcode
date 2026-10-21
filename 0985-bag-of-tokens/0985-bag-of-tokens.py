class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        
        left = 0
        right = len(tokens) - 1
        
        score = 0
        max_score = 0
        
        while left <= right:
            # Option 1: Play face-up (gain score, lose power)
            # If we have enough power to play the smallest token, it's always optimal
            # to play it face-up to gain a score point with minimum power cost.
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score) # Update max_score after every score gain
            # Option 2: Play face-down (lose score, gain power)
            # If we cannot play face-up (power is too low for the smallest token),
            # but we have at least one score point to sacrifice, and there are
            # other tokens remaining (left < right) to potentially use the gained power.
            # We should trade a score point for power by playing the largest token face-down
            # to maximize the power gained.
            elif score >= 1 and left < right:
                power += tokens[right]
                score -= 1
                right -= 1
            # Option 3: Cannot make any productive move
            # If power is too low for the smallest token AND
            # (score is 0 OR there are no other tokens left to make a profitable power trade),
            # then we are stuck and cannot improve our score.
            else:
                break
                
        return max_score