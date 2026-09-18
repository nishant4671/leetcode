class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        first = [n] * 26
        last = [-1] * 26
        for i, ch in enumerate(s):
            idx = ord(ch) - 97
            if first[idx] == n:
                first[idx] = i
            last[idx] = i
        intervals = []
        for i, ch in enumerate(s):
            idx = ord(ch) - 97
            if i != first[idx]:
                continue
            l, r = first[idx], last[idx]
            j = l
            while j <= r:
                cidx = ord(s[j]) - 97
                if first[cidx] < l:
                    l = first[cidx]
                    j = l
                    continue
                if last[cidx] > r:
                    r = last[cidx]
                j += 1
            intervals.append((l, r))
        intervals.sort(key=lambda x: x[1])
        res = []
        prev_end = -1
        for l, r in intervals:
            if l > prev_end:
                res.append(s[l:r+1])
                prev_end = r
        return res