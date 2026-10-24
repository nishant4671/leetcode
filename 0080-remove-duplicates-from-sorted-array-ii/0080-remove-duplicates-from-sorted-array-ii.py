class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        # k is the slow-pointer, representing the next position to write a valid element.
        # It also represents the count of valid elements.
        # The first two elements (nums[0] and nums[1]) are always considered valid
        # as per the problem's "at most twice" rule.
        # So, we initialize k to 2.
        k = 2

        # Iterate from the third element (index 2) onwards with the fast-pointer i.
        for i in range(2, len(nums)):
            # An element nums[i] should be kept if it is different from the element
            # at index k-2.
            # This logic ensures that we keep at most two occurrences of any number:
            # - If nums[i] is a new distinct number, it will be greater than nums[k-2].
            # - If nums[i] is the second occurrence of the number stored at nums[k-1],
            #   then nums[k-1] would be different from nums[k-2] (e.g., [..., 1, 2]).
            #   In this case, nums[i] will be equal to nums[k-1] but greater than nums[k-2],
            #   so it's copied.
            # - If nums[i] is the third or more occurrence of the number stored at nums[k-1],
            #   then nums[k-1] would be equal to nums[k-2] (e.g., [..., 2, 2]).
            #   In this case, nums[i] will be equal to nums[k-1] (and nums[k-2]),
            #   so nums[i] > nums[k-2] will be false, and it won't be copied.
            if nums[i] > nums[k-2]:
                nums[k] = nums[i]
                k += 1
        
        return k