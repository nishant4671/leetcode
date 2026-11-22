class Solution:
    def checkString(self, s: str) -> bool:
        found_b = False
        for char in s:
            if char == 'a':
                if found_b:
                    return False
            else: # char == 'b'
                found_b = True
        return True