class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagrams must have the same length.
        if len(s) != len(t):
            return False

        # Use an array to store character counts.
        # Since s and t consist of lowercase English letters,
        # we can use an array of size 26.
        # Index 0 for 'a', 1 for 'b', ..., 25 for 'z'.
        char_counts = [0] * 26

        # Iterate through string s and increment counts for each character.
        for char_s in s:
            # Convert character to its corresponding 0-25 index.
            # E.g., ord('a') - ord('a') = 0, ord('b') - ord('a') = 1
            char_counts[ord(char_s) - ord('a')] += 1
        
        # Iterate through string t and decrement counts for each character.
        # If a count drops below zero, it means t has more of that character
        # than s, so it cannot be an anagram.
        for char_t in t:
            index = ord(char_t) - ord('a')
            char_counts[index] -= 1
            if char_counts[index] < 0:
                return False
        
        # If we reach this point, it means:
        # 1. len(s) == len(t)
        # 2. No character in t caused its count to drop below zero (i.e., s had enough of each character).
        # These two conditions together imply that all characters in t were perfectly
        # matched by characters in s. Therefore, t is an anagram of s, and all counts
        # in `char_counts` must have balanced out to zero.
        return True