class Solution:
    def movesToMakeZigzag(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        # Calculate cost for the first pattern: even-indexed elements are peaks
        # A[0] > A[1] < A[2] > A[3] ...
        cost1 = self._calculate_cost(nums, True)

        # Calculate cost for the second pattern: odd-indexed elements are peaks
        # A[0] < A[1] > A[2] < A[3] ...
        cost2 = self._calculate_cost(nums, False)

        return min(cost1, cost2)

    def _calculate_cost(self, nums: list[int], even_indices_are_peaks: bool) -> int:
        cost = 0
        n = len(nums)
        arr = list(nums) # Create a mutable copy to apply conceptual changes

        for i in range(n):
            # Determine if current index should be a peak or valley based on the pattern
            is_current_idx_peak = (i % 2 == 0) if even_indices_are_peaks else (i % 2 != 0)

            if is_current_idx_peak: # Current element arr[i] should be a peak
                                   # (strictly greater than its neighbors, if they exist)
                # This implies its neighbors arr[i-1] and arr[i+1] must be <= arr[i]-1.
                
                # Check left neighbor
                if i > 0:
                    # If arr[i-1] is not strictly smaller than arr[i], it needs to be decreased.
                    if arr[i-1] >= arr[i]:
                        # Calculate how much arr[i-1] needs to be decreased to become arr[i]-1.
                        moves_needed = arr[i-1] - (arr[i] - 1)
                        cost += moves_needed
                        arr[i-1] -= moves_needed # Apply the conceptual decrease for subsequent checks
                
                # Check right neighbor
                if i < n - 1:
                    # If arr[i+1] is not strictly smaller than arr[i], it needs to be decreased.
                    if arr[i+1] >= arr[i]:
                        # Calculate how much arr[i+1] needs to be decreased to become arr[i]-1.
                        moves_needed = arr[i+1] - (arr[i] - 1)
                        cost += moves_needed
                        arr[i+1] -= moves_needed # Apply the conceptual decrease for subsequent checks
            
            else: # Current element arr[i] should be a valley
                  # (strictly smaller than its neighbors, if they exist)
                # This implies arr[i] must be at most min(arr[i-1], arr[i+1]) - 1.
                
                # Find the minimum value among its existing neighbors.
                # Use float('inf') as a sentinel for non-existent neighbors to not affect the minimum.
                min_neighbor_val = float('inf') 
                if i > 0:
                    min_neighbor_val = min(min_neighbor_val, arr[i-1])
                if i < n - 1:
                    min_neighbor_val = min(min_neighbor_val, arr[i+1])
                
                # If arr[i] is not strictly smaller than its minimum neighbor, it needs to be decreased.
                # Note: `min_neighbor_val` will be `float('inf')` if `n=1`.
                # This case is handled by the initial `if n <= 1: return 0`.
                if arr[i] >= min_neighbor_val:
                    # Calculate how much arr[i] needs to be decreased to become min_neighbor_val - 1.
                    moves_needed = arr[i] - (min_neighbor_val - 1)
                    cost += moves_needed
                    arr[i] -= moves_needed # Apply the conceptual decrease for subsequent checks
        
        return cost