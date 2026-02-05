# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

# The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.



class Solution(object):
    def removeDuplicates(self, nums):
        if not nums: #handles empty array case 
            return 0

        k = 1  # index for next unique position  here the first element is alwsays unique
#         #Meaning of k:

# “Next position where a new unique element should be placed”

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k
    





#     Loop walkthrough (step by step)
# 🔹 i = 1
# nums[i] = 1
# nums[i-1] = 1


# They are equal → duplicate

# ❌ Do nothing

# State:

# nums = [1, 1, 2, 2, 3]
# k = 1

# 🔹 i = 2
# nums[i] = 2
# nums[i-1] = 1


# Different → new unique element ✅

# nums[k] = nums[i]   # nums[1] = 2
# k += 1              # k = 2


# State:

# nums = [1, 2, 2, 2, 3]
# k = 2


# ✔ We overwrote a duplicate with a new unique value.

# 🔹 i = 3
# nums[i] = 2
# nums[i-1] = 2


# Same → duplicate

# ❌ Do nothing

# State:

# nums = [1, 2, 2, 2, 3]
# k = 2

# 🔹 i = 4
# nums[i] = 3
# nums[i-1] = 2


# Different → new unique element ✅

# nums[k] = nums[i]   # nums[2] = 3
# k += 1              # k = 3


# Final state:

# nums = [1, 2, 3, 2, 3]
# k = 3

# ✅ Final Result
# return k  # 3




