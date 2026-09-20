class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        # Initialize two candidates and their counts.
        # There can be at most two elements that appear more than n/3 times.
        # This is a variation of the Boyer-Moore Majority Vote Algorithm.
        candidate1, count1 = None, 0
        candidate2, count2 = None, 0

        # First pass: find potential candidates
        for num in nums:
            if num == candidate1:
                # If current number matches candidate1, increment its count
                count1 += 1
            elif num == candidate2:
                # If current number matches candidate2, increment its count
                count2 += 1
            elif count1 == 0:
                # If count1 is zero, assign current number as candidate1
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                # If count2 is zero, assign current number as candidate2
                candidate2 = num
                count2 = 1
            else:
                # If current number is different from both candidates, and both counts are > 0
                # decrement both counts. This effectively "cancels out" three distinct elements.
                count1 -= 1
                count2 -= 1

        # Second pass: verify the actual counts of the potential candidates
        # The first pass only gives candidates; it doesn't guarantee they are majority elements.
        count_c1 = 0
        count_c2 = 0
        for num in nums:
            if num == candidate1:
                count_c1 += 1
            elif num == candidate2:
                # Use elif to ensure a number is counted only once, even if candidate1 and candidate2
                # could theoretically refer to the same value (though unlikely with the logic above).
                count_c2 += 1
        
        result = []
        n = len(nums)
        
        # Calculate the threshold for majority
        n_by_3 = n // 3
        
        # Check if candidate1 meets the majority threshold
        # candidate1 could be None if the array was empty or contained too few elements for it to be assigned,
        # or if its count eventually dropped to zero and it wasn't replaced by another candidate.
        if candidate1 is not None and count_c1 > n_by_3:
            result.append(candidate1)
        
        # Check if candidate2 meets the majority threshold
        # Similar considerations for candidate2 being None.
        if candidate2 is not None and count_c2 > n_by_3:
            result.append(candidate2)
            
        return result