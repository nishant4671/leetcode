class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
# theory 
# ow this maps to your logic

# You were already doing these things (almost):

# Your Idea	Correct Version
# Track characters	seen = set()
# Window start (k)	left
# Loop index (i)	right
# Remove on duplicate	while duplicate → shrink
# Track max length	max_length
# The one missing concept you struggled with:

# Duplicate removal must repeat until the window is valid again

# That’s why this line is the heart of the solution:

# while s[right] in seen:


# Not if.
# While.

# 🔁 Step-by-step on "pwwkew"
# right=0 → p → seen={p} → max=1
# right=1 → w → seen={p,w} → max=2
# right=2 → w → duplicate!
#     remove p
#     remove w
#     add w → seen={w}
# right=3 → k → seen={w,k} → max=2
# right=4 → e → seen={w,k,e} → max=3
# right=5 → w → duplicate!
#     remove w
#     add w → seen={k,e,w}


# Answer = 3

# ⏱️ Complexity (important for interviews)

# Time: O(n)

# Space: O(min(n, charset))

# This is the best possible solution.
