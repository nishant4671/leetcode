class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum_of_squares = 0

        # Iterate through possible 1-indexed positions from 1 to n
        for i in range(1, n + 1):
            # Check if the current 1-indexed position 'i' divides 'n'
            if n % i == 0:
                # If 'i' divides 'n', the element nums[i] (1-indexed) is special.
                # In a 0-indexed Python list, this element is at index i-1.
                element_value = nums[i - 1]
                total_sum_of_squares += element_value * element_value
        
        return total_sum_of_squares