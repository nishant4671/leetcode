class Solution:
    def sumBase(self, n: int, k: int) -> int:
        total_sum = 0
        while n > 0:
            digit = n % k
            total_sum += digit
            n //= k
        return total_sum