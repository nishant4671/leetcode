class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left_rem = right_rem = 0
        for c in s:
            if c == '(':
                left_rem += 1
            elif c == ')':
                if left_rem == 0:
                    right_rem += 1
                else:
                    left_rem -= 1
        res = set()
        n = len(s)
        from functools import lru_cache
        @lru_cache(None)
        def dfs(i, left, right, bal):
            if i == n:
                if left == 0 and right == 0 and bal == 0:
                    return {""}
                return set()
            c = s[i]
            ans = set()
            if c == '(':
                if left > 0:
                    ans |= dfs(i+1, left-1, right, bal)
                ans_keep = dfs(i+1, left, right, bal+1)
                for sub in ans_keep:
                    ans.add('(' + sub)
            elif c == ')':
                if right > 0:
                    ans |= dfs(i+1, left, right-1, bal)
                if bal > 0:
                    ans_keep = dfs(i+1, left, right, bal-1)
                    for sub in ans_keep:
                        ans.add(')' + sub)
            else:
                ans_keep = dfs(i+1, left, right, bal)
                for sub in ans_keep:
                    ans.add(c + sub)
            return ans
        return list(dfs(0, left_rem, right_rem, 0))