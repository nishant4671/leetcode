class Solution:
    def sortableIntegers(self, nums):
        n = len(nums)
        s = sorted(nums)
        divs = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                divs.append(i)
                if i != n // i:
                    divs.append(n // i)
            i += 1
        def is_rotation(A, B):
            k = len(A)
            if k != len(B):
                return False
            if k == 0:
                return True
            # KMP preprocessing for pattern A
            lps = [0] * k
            length = 0
            idx = 1
            while idx < k:
                if A[idx] == A[length]:
                    length += 1
                    lps[idx] = length
                    idx += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[idx] = 0
                        idx += 1
            # search A in B+B
            text = B + B
            i = j = 0
            n2 = len(text)
            while i < n2:
                if A[j] == text[i]:
                    i += 1
                    j += 1
                    if j == k:
                        return True
                else:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1
            return False
        total = 0
        for k in divs:
            ok = True
            for start in range(0, n, k):
                if not is_rotation(nums[start:start + k], s[start:start + k]):
                    ok = False
                    break
            if ok:
                total += k
        return total