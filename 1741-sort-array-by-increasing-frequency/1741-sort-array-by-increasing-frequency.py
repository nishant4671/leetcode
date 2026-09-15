class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        import collections

        # Count the frequency of each number in the input list.
        freq_map = collections.Counter(nums)

        # Sort the original nums list using a custom key.
        # The key for sorting is a tuple (frequency, -value).
        # Python's default tuple sorting logic applies:
        # 1. It compares the first elements of the tuples. Here, `freq_map[x]`
        #    This sorts by frequency in increasing order.
        # 2. If the first elements are equal (i.e., frequencies are the same),
        #    it then compares the second elements. Here, `-x`.
        #    By negating `x`, we achieve sorting by value in decreasing order.
        #    For example, if frequencies are equal for 2 and 3:
        #    (freq, -3) will come before (freq, -2) because -3 < -2.
        nums.sort(key=lambda x: (freq_map[x], -x))

        # Return the sorted list. The `nums.sort()` method sorts the list in-place.
        return nums