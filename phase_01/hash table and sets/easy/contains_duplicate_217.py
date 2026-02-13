# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen.add(nums[i])
        return False