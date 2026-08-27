class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        rem = [0] * 26
        for ch in s:
            rem[ord(ch) - ord('a')] += 1
            
        k = 0
        while k < n and rem[ord(target[k]) - ord('a')] > 0:
            rem[ord(target[k]) - ord('a')] -= 1
            k += 1
            
        if k == n:
            k = n - 1
            rem[ord(target[n - 1]) - ord('a')] += 1
            
        for i in range(k, -1, -1):
            target_char_code = ord(target[i]) - ord('a')
            c_code = -1
            for code in range(target_char_code + 1, 26):
                if rem[code] > 0:
                    c_code = code
                    break
            
            if c_code != -1:
                rem[c_code] -= 1
                suffix = []
                for code in range(26):
                    if rem[code] > 0:
                        suffix.append(chr(ord('a') + code) * rem[code])
                return target[:i] + chr(ord('a') + c_code) + "".join(suffix)
            
            if i > 0:
                rem[ord(target[i - 1]) - ord('a')] += 1
                
        return ""