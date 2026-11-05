import bisect

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        
        distance_value = 0
        
        for num1 in arr1:
            # The condition to check for each num1 is if there exists any num2 in arr2 such that:
            # |num1 - num2| <= d
            # This inequality can be rewritten as:
            # -d <= num1 - num2 <= d
            # Rearranging it to isolate num2 gives the range:
            # num1 - d <= num2 <= num1 + d
            
            # We need to determine if any element num2 in arr2 falls within the range [num1 - d, num1 + d].
            # Since arr2 is sorted, we can use binary search to efficiently check this.
            
            # bisect_left(arr2, target) returns an insertion point which is the index
            # of the first element in arr2 that is greater than or equal to `target`.
            # Here, `target` is `num1 - d`.
            idx = bisect.bisect_left(arr2, num1 - d)
            
            # If `idx` is a valid index within `arr2` (i.e., `idx < len(arr2)`)
            # AND the element at `arr2[idx]` is less than or equal to `num1 + d`,
            # it means we have found an element `arr2[idx]` such that:
            # num1 - d <= arr2[idx] <= num1 + d
            # In this scenario, `num1` does NOT satisfy the distance condition,
            # so we do not increment `distance_value`.
            
            # Otherwise, if no such `arr2[idx]` is found (either `idx == len(arr2)` meaning all elements
            # in `arr2` are smaller than `num1 - d`, or `arr2[idx] > num1 + d` meaning the first
            # element that is >= `num1 - d` is already too large), then `num1` satisfies
            # the distance condition, and we increment `distance_value`.

            found_close_element = False
            if idx < len(arr2):
                if arr2[idx] <= num1 + d:
                    found_close_element = True
            
            if not found_close_element:
                distance_value += 1
                
        return distance_value