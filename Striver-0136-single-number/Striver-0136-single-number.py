class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initialize a variable to accumulate the XOR sum.
        # XORing any number with 0 yields the number itself,
        # so 0 is a neutral starting point.
        xor_sum = 0

        # Iterate through each number in the input array.
        for num in nums:
            # Perform a bitwise XOR operation between the current number
            # and the running xor_sum.
            # The key properties of XOR used here are:
            # 1. A ^ A = 0 (A number XORed with itself is 0)
            # 2. A ^ 0 = A (A number XORed with 0 is the number itself)
            # Due to these properties, all numbers that appear twice will
            # effectively cancel each other out (XORing to 0).
            # The single unique number, which appears only once, will remain
            # as the final xor_sum.
            xor_sum ^= num

        # After iterating through all numbers, xor_sum will contain
        # the single number that appears only once.
        return xor_sum