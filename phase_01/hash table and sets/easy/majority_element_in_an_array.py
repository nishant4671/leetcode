# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

class Solution(object):
    def majorityElement(self, nums):
        count_of_elements = {}
        
        # Count occurrences of each element
        for i in range(len(nums)):
            if nums[i] in count_of_elements:
                count_of_elements[nums[i]] += 1
            else:
                count_of_elements[nums[i]] = 1
        
        # Find the majority element
        for key in count_of_elements:
            if count_of_elements[key] > len(nums) // 2:  # Strictly greater than n/2
                return key
        
        return None  # This line will never be reached (problem guarantees majority exists)
