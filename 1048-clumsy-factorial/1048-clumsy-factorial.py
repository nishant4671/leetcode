class Solution:
    def clumsy(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 6
        if n == 4:
            return 7
        
        remainder = n % 4
        
        if remainder == 0:
            return n + 1
        elif remainder == 1:
            return n + 2
        elif remainder == 2:
            return n + 2
        else:  # remainder == 3
            return n - 1