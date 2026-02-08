# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.





class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left+right)//2

            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left = mid+1
            else :
                right = mid-1

        return left                   



        # theory of this solution is to use binary search to find the target value in the sorted array. If the target value is found, we return its index. If it is not found, we return the index where it would be inserted in order to maintain the sorted order of the array. The time complexity of this solution is O(log n) due to the binary search algorithm used.
