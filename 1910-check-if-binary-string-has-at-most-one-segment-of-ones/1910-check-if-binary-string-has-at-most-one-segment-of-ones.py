class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        seen_zero = False
        for char in s:
            if char == '1':
                if seen_zero:
                    return False
            else:
                seen_zero = True
        return True