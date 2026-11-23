class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        num_required_codes = 1 << k
        found_codes = set()
        
        current_hash = 0
        bit_mask = (1 << k) - 1
        
        for i in range(len(s)):
            current_hash = (current_hash << 1) | int(s[i])
            
            if i >= k - 1:
                masked_code = current_hash & bit_mask
                found_codes.add(masked_code)
                
                if len(found_codes) == num_required_codes:
                    return True
        
        return False