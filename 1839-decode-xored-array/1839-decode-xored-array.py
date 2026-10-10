class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        n = len(encoded) + 1
        arr = [0] * n
        arr[0] = first
        for i in range(n - 1):
            arr[i+1] = encoded[i] ^ arr[i]
        return arr