import collections

class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Count the frequency of each character in the string.
        # collections.Counter efficiently creates a dictionary-like object 
        # mapping characters to their counts.
        char_counts = collections.Counter(s)

        # Step 2 & 3: Sort characters by frequency in decreasing order and construct the result string.
        # char_counts.items() yields (character, count) pairs.
        # sorted() sorts these pairs. The key for sorting is the frequency (item[1]),
        # and reverse=True ensures sorting in descending order of frequency.
        # A list comprehension then generates strings like 'e'*2 for ('e', 2), etc.
        # Finally, "".join() concatenates all these generated strings into a single result.
        return "".join([char * count for char, count in sorted(char_counts.items(), key=lambda item: item[1], reverse=True)])