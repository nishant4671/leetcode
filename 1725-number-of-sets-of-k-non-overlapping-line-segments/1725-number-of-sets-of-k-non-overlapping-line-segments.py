class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        MAX_COMB_N_VAL = n + k - 1
        
        fact = [1] * (MAX_COMB_N_VAL + 1)
        inv_fact = [1] * (MAX_COMB_N_VAL + 1)

        for i in range(1, MAX_COMB_N_VAL + 1):
            fact[i] = (fact[i-1] * i) % MOD
        
        def power(base, exp):
            res = 1
            base %= MOD
            while exp > 0:
                if exp % 2 == 1:
                    res = (res * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return res

        inv_fact[MAX_COMB_N_VAL] = power(fact[MAX_COMB_N_VAL], MOD - 2)
        for i in range(MAX_COMB_N_VAL - 1, -1, -1):
            inv_fact[i] = (inv_fact[i+1] * (i+1)) % MOD

        def nCr_mod_p(n_val, r_val):
            if r_val < 0 or r_val > n_val:
                return 0
            num = fact[n_val]
            den = (inv_fact[r_val] * inv_fact[n_val - r_val]) % MOD
            return (num * den) % MOD

        return nCr_mod_p(n + k - 1, 2 * k)