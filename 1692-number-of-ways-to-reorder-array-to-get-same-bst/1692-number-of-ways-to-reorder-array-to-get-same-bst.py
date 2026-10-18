class Solution:
    def numOfWays(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD
        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD
        def dfs(arr):
            if len(arr) <= 2:
                return len(arr), 1
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            lsize, lways = dfs(left)
            rsize, rways = dfs(right)
            total = comb(lsize + rsize, lsize) * lways % MOD * rways % MOD
            return lsize + rsize + 1, total
        _, totalWays = dfs(nums)
        return (totalWays - 1) % MOD