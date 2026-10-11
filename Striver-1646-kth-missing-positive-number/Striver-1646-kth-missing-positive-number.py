class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        n = len(arr)
        
        # Binary search for the smallest index 'ans_idx' such that
        # the number of missing positives up to arr[ans_idx] is at least k.
        # The number of missing positives up to arr[i] is arr[i] - (i + 1).
        
        low = 0
        high = n - 1
        
        # 'ans_idx' will store the index of the first element `arr[ans_idx]`
        # where the cumulative count of missing numbers is `>= k`.
        # If all numbers in `arr` result in `missing_count < k`, then `ans_idx` will be `n`.
        ans_idx = n 
        
        while low <= high:
            mid = low + (high - low) // 2
            
            # Calculate the number of missing positive integers up to arr[mid].
            # If arr[mid] was the (mid+1)-th positive integer (i.e., if no numbers were missing before it),
            # then it would be equal to (mid+1).
            # The difference arr[mid] - (mid+1) gives the actual count of missing positive integers
            # before or at arr[mid].
            missing_count = arr[mid] - (mid + 1)
            
            if missing_count >= k:
                # The k-th missing number is at or before arr[mid].
                # Store this `mid` as a potential answer and try to find an earlier `mid`.
                ans_idx = mid
                high = mid - 1
            else:
                # The k-th missing number is after arr[mid].
                # Not enough missing numbers found yet, search in the right half.
                low = mid + 1
        
        # After the binary search loop, 'ans_idx' holds the smallest index `i`
        # such that `arr[i] - (i + 1) >= k`.
        # This means that the k-th missing positive integer is greater than `arr[ans_idx - 1]`
        # (if `ans_idx > 0`) and less than or equal to `arr[ans_idx]`.
        # Alternatively, if `ans_idx` is `n`, it means all elements in `arr` have
        # `missing_count < k`. So, the k-th missing number is after `arr[n-1]`.
        
        # Let `X` be the k-th missing positive integer.
        # Let `count_present_less_than_X` be the count of numbers in `arr` that are strictly less than `X`.
        # We derived that `X = k + count_present_less_than_X`.
        
        # From the binary search, `ans_idx` is exactly `count_present_less_than_X`.
        # This holds for both cases:
        # 1. If `ans_idx = 0`, it means `arr[0]` is already "too large" or is the first.
        #    `count_present_less_than_X` is 0. Our `ans_idx` is 0.
        # 2. If `ans_idx > 0`, it means `arr[ans_idx - 1]` is the last element whose `missing_count` was `< k`.
        #    All elements `arr[0], ..., arr[ans_idx - 1]` are strictly less than `X`.
        #    There are `ans_idx` such elements. So, `count_present_less_than_X = ans_idx`.
        
        # Therefore, the k-th missing positive integer is `k + ans_idx`.
        return k + ans_idx