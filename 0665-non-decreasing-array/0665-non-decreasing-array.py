class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        modifications = 0

        for i in range(n - 1):
            if nums[i] > nums[i+1]:
                modifications += 1
                if modifications > 1:
                    return False
                
                # We have found one violation at index i where nums[i] > nums[i+1].
                # We must modify either nums[i] or nums[i+1].

                # If i is 0, we can always modify nums[0] to nums[1] without creating a violation
                # with a non-existent nums[-1]. This is always a safe choice for nums[i].
                # If i > 0, we need to consider nums[i-1].
                # If nums[i-1] <= nums[i+1], it means we can decrease nums[i] to nums[i+1]
                # without violating the non-decreasing property with nums[i-1].
                # This is generally preferred because decreasing nums[i] (making it nums[i+1])
                # keeps nums[i+1] as small as possible, which is beneficial for future checks (nums[i+1] <= nums[i+2]).
                
                # However, if nums[i-1] > nums[i+1], decreasing nums[i] to nums[i+1]
                # would create a new violation (nums[i-1] > new_nums[i]).
                # In this specific scenario, we *must* increase nums[i+1] to nums[i].
                
                if i > 0 and nums[i-1] > nums[i+1]:
                    # This case means modifying nums[i] would create a new violation to its left.
                    # So, we are forced to modify nums[i+1].
                    nums[i+1] = nums[i]
                else:
                    # This case covers i == 0, or nums[i-1] <= nums[i+1].
                    # In both scenarios, it is safe and generally better to modify nums[i].
                    nums[i] = nums[i+1]
        
        return True