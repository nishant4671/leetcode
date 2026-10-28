class Solution:
    def largestTimeFromDigits(self, arr: list[int]) -> str:
        max_time_str = ""
        
        import itertools
        
        for p in itertools.permutations(arr):
            h1, h2, m1, m2 = p
            
            hours = h1 * 10 + h2
            minutes = m1 * 10 + m2
            
            if 0 <= hours <= 23 and 0 <= minutes <= 59:
                current_time = f"{hours:02d}:{minutes:02d}"
                if max_time_str == "" or current_time > max_time_str:
                    max_time_str = current_time
        
        return max_time_str