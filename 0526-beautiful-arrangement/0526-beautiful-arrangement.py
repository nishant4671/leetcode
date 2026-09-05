class Solution:
    def countArrangement(self, n: int) -> int:
        import functools

        @functools.lru_cache(None)
        def dfs(index: int, mask: int) -> int:
            if index > n:
                return 1
            
            count = 0
            for num in range(1, n + 1):
                # Check if 'num' has not been used yet
                # The (num-1)-th bit in 'mask' corresponds to number 'num'
                if not ((mask >> (num - 1)) & 1):
                    # Check the beautiful arrangement condition:
                    # perm[index] = num
                    # (num % index == 0) OR (index % num == 0)
                    if num % index == 0 or index % num == 0:
                        # If condition met, place 'num' at 'index'
                        # Mark 'num' as used by setting its bit in the mask
                        count += dfs(index + 1, mask | (1 << (num - 1)))
            return count
        
        # Start the recursion from the first position (index = 1)
        # with an empty mask (no numbers used yet).
        return dfs(1, 0)