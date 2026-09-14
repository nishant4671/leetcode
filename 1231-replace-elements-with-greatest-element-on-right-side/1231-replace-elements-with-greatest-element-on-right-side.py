class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        
        # Initialize max_right_so_far to -1. 
        # This serves two purposes:
        # 1. It's the required replacement value for the last element.
        # 2. It correctly initializes the maximum for elements to the left, as any valid array element
        #    (1 <= arr[i] <= 10^5) will be greater than -1.
        max_right_so_far = -1
        
        # Iterate from the last element (index n-1) down to the first element (index 0).
        # We process the array in reverse order to efficiently maintain the maximum element
        # encountered so far to the right of the current position.
        for i in range(n - 1, -1, -1):
            # Store the current element's original value. This value will be used
            # to potentially update `max_right_so_far` for elements further to its left.
            original_current_element = arr[i]
            
            # Replace the current element with the `max_right_so_far` value computed
            # from the previous iteration (i.e., the maximum of elements to its right).
            # For the very last element (i=n-1), this will assign -1.
            arr[i] = max_right_so_far
            
            # Update `max_right_so_far`. The new `max_right_so_far` for elements
            # at index `i-1` and further left must consider the original value of `arr[i]`
            # as a potential candidate for the maximum.
            max_right_so_far = max(max_right_so_far, original_current_element)
            
        return arr