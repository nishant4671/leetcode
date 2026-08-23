class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2
        
        sum_l = q_l = 0
        sum_r = q_r = 0
        
        for i in range(mid):
            if num[i] == '?':
                q_l += 1
            else:
                sum_l += int(num[i])
                
        for i in range(mid, n):
            if num[i] == '?':
                q_r += 1
            else:
                sum_r += int(num[i])
        
        # If total number of '?' is odd, Alice always makes the last move and wins
        if (q_l + q_r) % 2 == 1:
            return True
        
        # Bob wins if and only if the difference in known sums balances out 
        # the remaining question mark pairs on one side (each pair contributes 9)
        diff_sum = sum_l - sum_r
        diff_q = q_r - q_l
        
        return diff_sum * 2 != diff_q * 9