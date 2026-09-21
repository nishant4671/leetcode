class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Step 1: Sort the array
        nums.sort()
        
        results = []
        n = len(nums)
        
        # Step 2: Iterate through the array to fix the first element (nums[i])
        # We iterate up to n-2 because we need at least two more elements (nums[left] and nums[right])
        for i in range(n - 2):
            # Optimization 1: Skip duplicate values for nums[i]
            # If the current nums[i] is the same as the previous one,
            # any triplets formed with nums[i] would be duplicates of triplets
            # formed with nums[i-1]. So, we skip this nums[i].
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Optimization 2: If nums[i] is already positive, and the array is sorted,
            # then nums[left] and nums[right] (where left > i, right > left)
            # will also be non-negative. Their sum (nums[i] + nums[left] + nums[right])
            # will definitely be greater than 0. So, no need to check further.
            if nums[i] > 0:
                break
            
            # Step 3: Use two pointers (left and right) for the remaining part of the array
            # We need to find nums[left] + nums[right] such that nums[i] + nums[left] + nums[right] == 0.
            # This means nums[left] + nums[right] == -nums[i].
            target = -nums[i]
            left, right = i + 1, n - 1 # Left pointer starts after i, right pointer starts at the end
            
            # Step 4: Two-pointer search
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    # Found a triplet that sums to zero
                    results.append([nums[i], nums[left], nums[right]])
                    
                    # Move both pointers to look for new distinct pairs
                    left += 1
                    right -= 1
                    
                    # Optimization 3: Skip duplicate values for nums[left] and nums[right]
                    # After finding a valid triplet, we need to skip any immediate duplicates
                    # for nums[left] and nums[right] to ensure that the next triplet found
                    # is unique.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current_sum < target:
                    # Current sum is too small, need a larger number.
                    # Move the left pointer to the right to increase the sum.
                    left += 1
                else: # current_sum > target
                    # Current sum is too large, need a smaller number.
                    # Move the right pointer to the left to decrease the sum.
                    right -= 1
        
        return results