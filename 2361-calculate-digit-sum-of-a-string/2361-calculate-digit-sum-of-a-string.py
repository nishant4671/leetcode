class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            next_s_parts = []
            
            for i in range(0, len(s), k):
                group = s[i : i + k]
                
                current_sum = 0
                for char_digit in group:
                    current_sum += int(char_digit)
                
                next_s_parts.append(str(current_sum))
            
            s = "".join(next_s_parts)
        
        return s