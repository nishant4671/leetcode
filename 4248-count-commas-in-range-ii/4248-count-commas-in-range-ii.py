class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        k = 1  # current number of commas
        
        # `power_of_10` represents 10^(3*k). 
        # For k=1, numbers start having 1 comma from 10^3 (1,000).
        # So, we initialize `power_of_10` to 1000.
        power_of_10 = 1000 

        while True:
            # `range_start` is the smallest number that has `k` commas.
            # For k=1, range_start = 1000.
            # For k=2, range_start = 1000000.
            range_start = power_of_10

            # If `n` is smaller than `range_start`, it means no numbers up to `n` 
            # have `k` or more commas. So, we can stop.
            if n < range_start:
                break

            # `next_power_of_10` is the threshold for numbers that would have `k+1` commas.
            # E.g., for k=1, next_power_of_10 = 10^6 (1,000,000).
            # Numbers from `range_start` up to `next_power_of_10 - 1` have `k` commas.
            next_power_of_10 = power_of_10 * 1000
            
            # `current_range_upper_bound` is the maximum number to consider for `k` commas,
            # limited by `n`.
            # This is `min(n, largest_number_with_k_commas)`.
            # The largest number with `k` commas is `next_power_of_10 - 1`.
            current_range_upper_bound = min(n, next_power_of_10 - 1)
            
            # Calculate how many numbers within this range actually contribute `k` commas.
            # These are numbers from `range_start` up to `current_range_upper_bound`.
            num_count_in_range = current_range_upper_bound - range_start + 1
            
            # Add the commas for these numbers to the total.
            total_commas += num_count_in_range * k
            
            # If `n` falls within the current `k`-comma range (i.e., `n` is less than 
            # the next threshold `next_power_of_10`), we have counted all commas up to `n`.
            if n < next_power_of_10:
                break

            # Move to consider the next number of commas.
            k += 1
            # Update `power_of_10` for the next iteration.
            # E.g., from 10^3 (for k=1) to 10^6 (for k=2).
            power_of_10 = next_power_of_10

        return total_commas