class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        
        # This is the recursive merge sort function
        # It takes a sub-array defined by its 'low' and 'high' indices,
        # sorts it, and returns the number of reverse pairs found within it.
        def merge_sort_and_count(arr, low, high):
            # Base case: if the sub-array has 0 or 1 elements, no reverse pairs
            if low >= high:
                return 0

            mid = low + (high - low) // 2
            
            # Recursively count pairs in the left and right halves
            # arr[low...mid] and arr[mid+1...high]
            count = merge_sort_and_count(arr, low, mid)
            count += merge_sort_and_count(arr, mid + 1, high)
            
            # Count pairs where i is in the left half and j is in the right half
            # These are the "cross-half" pairs that need to be counted during the merge step
            count += count_cross_pairs(arr, low, mid, high)
            
            # Merge the two sorted halves to form a single sorted sub-array
            # This step modifies 'arr' in-place, sorting the current segment.
            merge(arr, low, mid, high)
            
            return count

        # This function counts reverse pairs (i, j) where 'i' is in the left sub-array (arr[low...mid])
        # and 'j' is in the right sub-array (arr[mid+1...high]).
        # Both sub-arrays are assumed to be sorted before this call.
        def count_cross_pairs(arr, low, mid, high):
            pairs = 0
            j = mid + 1 # Pointer for the right half, starting at its beginning
            
            # Iterate through each element in the left half
            for i in range(low, mid + 1):
                # For the current arr[i] from the left half,
                # find all elements arr[j] in the right half such that arr[i] > 2 * arr[j]
                # The 'j' pointer only moves forward because both halves are sorted.
                # If arr[i] > 2 * arr[j], then arr[i] > 2 * arr[j'] for all j' < j
                # (since arr[j'] <= arr[j]).
                # This logic is key for the two-pointer approach for counting:
                # for a given arr[i], we find the first arr[j] that DOES NOT satisfy the condition.
                # All elements arr[mid+1]...arr[j-1] satisfy the condition.
                # Use long() for multiplication to prevent overflow if the numbers were standard 32-bit integers.
                # In Python, integers handle arbitrary precision, so this is not strictly necessary but
                # good practice for conceptual understanding in other languages.
                while j <= high and arr[i] > 2 * arr[j]:
                    j += 1
                
                # The number of elements in the right half that satisfy the condition with arr[i]
                # is (j - 1) - (mid + 1) + 1, which simplifies to j - (mid + 1).
                pairs += (j - (mid + 1)) 
            return pairs

        # This function merges two sorted sub-arrays: arr[low...mid] and arr[mid+1...high]
        # into a single sorted sub-array, stored back in arr[low...high].
        def merge(arr, low, mid, high):
            temp = [] # Temporary list to store the merged sorted elements
            p1 = low       # Pointer for the left sub-array (arr[low...mid])
            p2 = mid + 1   # Pointer for the right sub-array (arr[mid+1...high])

            # Compare elements from both sub-arrays and add the smaller one to 'temp'
            while p1 <= mid and p2 <= high:
                if arr[p1] <= arr[p2]:
                    temp.append(arr[p1])
                    p1 += 1
                else:
                    temp.append(arr[p2])
                    p2 += 1
            
            # Add any remaining elements from the left sub-array
            while p1 <= mid:
                temp.append(arr[p1])
                p1 += 1
            
            # Add any remaining elements from the right sub-array
            while p2 <= high:
                temp.append(arr[p2])
                p2 += 1
            
            # Copy the sorted elements from 'temp' back to the original array 'arr'
            for k in range(len(temp)):
                arr[low + k] = temp[k]

        # Initiate the merge sort process on the entire array
        return merge_sort_and_count(nums, 0, len(nums) - 1)