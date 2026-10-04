class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Initialize the search space.
        # low points to the first possible index (0).
        # high points to the last possible index (n-1).
        low = 0
        high = n - 1
        
        # Perform binary search until low and high converge to a single element.
        while low < high:
            # Calculate the middle index.
            # Using low + (high - low) // 2 avoids potential overflow for very large low/high,
            # though not strictly necessary for the given constraints (n <= 1000).
            mid = low + (high - low) // 2
            
            # Compare nums[mid] with its right neighbor, nums[mid+1].
            # The problem guarantees nums[i] != nums[i+1], so they cannot be equal.
            
            if nums[mid] < nums[mid+1]:
                # If nums[mid] is less than nums[mid+1], we are on an ascending slope.
                # This means a peak element must exist to the right of mid (inclusive of mid+1).
                # Therefore, we discard mid and everything to its left, and search in the right half.
                low = mid + 1
            else: # nums[mid] > nums[mid+1]
                # If nums[mid] is greater than nums[mid+1], we are either at a peak,
                # or on a descending slope from mid.
                # In this case, a peak element must exist at mid or to its left.
                # We discard elements to the right of mid+1 and search in the left half,
                # keeping mid as a potential peak candidate.
                high = mid
                
        # When the loop terminates, low == high.
        # This single index 'low' (or 'high') is guaranteed to be the index of a peak element.
        # This is because the invariant (a peak exists within [low, high]) is maintained
        # throughout the binary search process.
        return low