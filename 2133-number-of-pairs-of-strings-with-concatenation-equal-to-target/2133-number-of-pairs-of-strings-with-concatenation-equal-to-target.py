import collections

class Solution:
    def numOfPairs(self, nums: list[str], target: str) -> int:
        counts = collections.Counter(nums)
        
        total_pairs = 0
        
        for s1, count1 in counts.items():
            len1 = len(s1)
            
            if not target.startswith(s1):
                continue
            
            if len1 >= len(target):
                continue
            
            s2 = target[len1:]
            
            if s2 in counts:
                count2 = counts[s2]
                
                if s1 == s2:
                    total_pairs += count1 * (count1 - 1)
                else:
                    total_pairs += count1 * count2
                    
        return total_pairs