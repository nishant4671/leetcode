class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)

        if idx == -1:
            return word
        else:
            prefix_to_reverse = word[:idx+1]
            reversed_prefix = prefix_to_reverse[::-1]
            suffix = word[idx+1:]
            return reversed_prefix + suffix