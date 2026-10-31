class Solution:
    def maxStudents(self, seats):
        m, n = len(seats), len(seats[0])
        row_masks = []
        for i in range(m):
            avail = 0
            for j in range(n):
                if seats[i][j] == '.':
                    avail |= (1 << j)
            masks = []
            for mask in range(1 << n):
                if (mask & ~avail) != 0:
                    continue
                if (mask & (mask << 1)) != 0:
                    continue
                masks.append(mask)
            row_masks.append(masks)
        dp = {0: 0}
        for i in range(m):
            ndp = {}
            for mask in row_masks[i]:
                cnt = mask.bit_count()
                for pmask, val in dp.items():
                    if (mask << 1) & pmask: continue
                    if (mask >> 1) & pmask: continue
                    ndp[mask] = max(ndp.get(mask, 0), val + cnt)
            dp = ndp
        return max(dp.values()) if dp else 0