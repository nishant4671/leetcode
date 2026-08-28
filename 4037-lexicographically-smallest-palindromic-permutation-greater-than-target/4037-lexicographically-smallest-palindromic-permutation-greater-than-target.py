class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        from collections import Counter

        counts = Counter(s)
        odd_chars = [c for c, cnt in counts.items() if cnt % 2 != 0]

        if len(odd_chars) > 1:
            return ""

        mid_char = odd_chars[0] if odd_chars else ""
        half_counts = {c: counts[c] // 2 for c in counts}

        n = len(s)
        m = n // 2
        t1 = target[:m]

        t1_counts = Counter(t1)
        if all(t1_counts[c] <= half_counts.get(c, 0) for c in t1_counts):
            p = t1 + mid_char + t1[::-1]
            if p > target:
                return p

        for i in range(m - 1, -1, -1):
            t_pref = t1[:i]
            pref_counts = Counter(t_pref)
            if all(pref_counts[c] <= half_counts.get(c, 0) for c in pref_counts):
                rem_counts = {c: half_counts.get(c, 0) - pref_counts.get(c, 0) for c in half_counts}
                target_char = t1[i]
                
                next_char = None
                for c in sorted(rem_counts.keys()):
                    if c > target_char and rem_counts[c] > 0:
                        next_char = c
                        break
                
                if next_char:
                    rem_counts[next_char] -= 1
                    suffix = "".join(ch * rem_counts[ch] for ch in sorted(rem_counts.keys()))
                    p1 = t_pref + next_char + suffix
                    return p1 + mid_char + p1[::-1]

        return ""