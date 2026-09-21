class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        
        # current_counts[r] stores the number of contiguous subarrays ending at the previous element
        # whose product modulo k is r.
        current_counts = [0] * k 
        
        for num in nums:
            # next_counts will store counts for subarrays ending at the current 'num'
            next_counts = [0] * k
            
            # 1. The current 'num' itself forms a subarray.
            # Its product modulo k is (num % k).
            next_counts[num % k] += 1
            
            # 2. Extend subarrays that ended at the previous element.
            #    If a subarray ending at the previous element had product 'r_prev' modulo k,
            #    then appending 'num' to it forms a new subarray.
            #    Its product modulo k will be (r_prev * num) % k.
            for r_prev in range(k):
                if current_counts[r_prev] > 0:
                    new_rem = (r_prev * num) % k
                    next_counts[new_rem] += current_counts[r_prev]
            
            # Update current_counts for the next iteration.
            # These are now the counts for subarrays ending at the current 'num'.
            current_counts = next_counts
            
            # Add the counts for subarrays ending at the current 'num' to the total result.
            for r in range(k):
                result[r] += current_counts[r]
                
        return result