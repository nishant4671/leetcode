

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].




























class Solution(object):
    def searchRange(self, nums, target):
        nums.sort()

        for i in range(len(nums)):
            if target == nums[i]:
                starting_index_of_target = i
                indexes = []
                indexes.append(i)

                for j in range(i + 1, len(nums)):
                    if nums[j] == nums[starting_index_of_target]:
                        indexes.append(j)
                    else:
                        break

                print(indexes)
                return [indexes[0], indexes[-1]]

            if target < nums[i]:
                break

        return [-1, -1]



# theory :
# The problem can be solved by first sorting the array to ensure that the elements are in order.
# We then iterate through the sorted array to find the first occurrence of the target element.
# Once we find the first occurrence, we continue to check subsequent elements to find the last occurrence of the target.
# If the target is not found in the array, we return [-1, -1].
# We sort the input array to ensure it is in non-decreasing order.
# We then iterate through the sorted array to find the first and last positions of the target element.
# If the target is found, we store the starting index and continue to find the last index.
# If the target is not found, we return [-1, -1].
# We sort the input array to ensure it is in non-decreasing order.
# We then iterate through the sorted array to find the first and last positions of the target element.
