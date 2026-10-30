class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        total_steps = 0
        d = 2

        while d * d <= n:
            while n % d == 0:
                total_steps += d
                n //= d
            d += 1

        if n > 1:
            total_steps += n
            
        return total_steps