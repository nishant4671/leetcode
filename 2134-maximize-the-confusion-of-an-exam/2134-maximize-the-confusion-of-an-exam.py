class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        def find_max_consecutive(target_char: str) -> int:
            n = len(answerKey)
            left = 0
            max_len = 0
            flips_needed = 0

            for right in range(n):
                if answerKey[right] != target_char:
                    flips_needed += 1

                while flips_needed > k:
                    if answerKey[left] != target_char:
                        flips_needed -= 1
                    left += 1
                
                max_len = max(max_len, right - left + 1)
            
            return max_len

        max_t_consecutive = find_max_consecutive('T')
        max_f_consecutive = find_max_consecutive('F')
        
        return max(max_t_consecutive, max_f_consecutive)