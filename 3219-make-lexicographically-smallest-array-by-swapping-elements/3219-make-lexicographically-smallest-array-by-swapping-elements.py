class Solution:

    def lexicographicallySmallestArray(
        self, nums: List[int], limit: int
    ) -> List[int]:
        n = len(nums)
        sorted_pairs = sorted((val, i) for i, val in enumerate(nums))

        ans = [0] * n

        i = 0
        while i < n:
            j = i
            vals = [sorted_pairs[i][0]]
            indices = [sorted_pairs[i][1]]

            while (
                j + 1 < n
                and sorted_pairs[j + 1][0] - sorted_pairs[j][0] <= limit
            ):
                j += 1
                vals.append(sorted_pairs[j][0])
                indices.append(sorted_pairs[j][1])

            indices.sort()

            for k in range(len(vals)):
                ans[indices[k]] = vals[k]

            i = j + 1

        return ans