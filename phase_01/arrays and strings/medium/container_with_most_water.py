# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.



class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            area = width * current_height

            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area



# theory :
# The problem can be solved using a two-pointer approach. We start with two pointers, one at the beginning (left) and one at the end (right) of the height array. We calculate the area formed by the lines at these two pointers and update the maximum area found so far.
# We then move the pointer pointing to the shorter line inward, as moving the longer line inward cannot increase the area. We repeat this process until the two pointers meet.




# We use a two-pointer approach. One pointer starts at the left end and the other at the right end of the array.
# At each step, we calculate the area using the distance between the pointers as the width and the minimum of the two heights as the limiting height.
# We keep track of the maximum area seen so far.
# Then, we move the pointer with the smaller height inward, because the shorter line limits the water and moving the taller one cannot increase the area.