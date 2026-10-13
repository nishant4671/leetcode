class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        # State: current string configuration; distance = number of swaps performed.
        # BFS explores states level by level to guarantee minimal swaps.
        # Branching: at first mismatched index i, only swap with positions j>i where
        #   s1[j] matches target character s2[i] and swapping improves (s1[j]!=s2[j]).
        # This heuristic reduces search space while preserving optimality.
        # Time complexity: O(N! / (some factor)) in worst case, but with N≤20 and
        #   pruning it runs fast; practically O(b^d) where b is limited branching.
        # Space complexity: O(number of visited states) ≤ O(N!).
        if s1 == s2:
            return 0
        from collections import deque
        visited = {s1}
        q = deque([(s1, 0)])
        n = len(s1)
        while q:
            cur, steps = q.popleft()
            # find first index where cur differs from target
            i = 0
            while i < n and cur[i] == s2[i]:
                i += 1
            # try beneficial swaps
            for j in range(i + 1, n):
                if cur[j] == s2[i] and cur[j] != s2[j]:
                    lst = list(cur)
                    lst[i], lst[j] = lst[j], lst[i]
                    nxt = ''.join(lst)
                    if nxt == s2:
                        return steps + 1
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, steps + 1))
        return -1