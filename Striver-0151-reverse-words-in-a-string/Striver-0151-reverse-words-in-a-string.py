class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Split the string into a list of words.
        # s.split() without arguments automatically handles multiple spaces
        # and leading/trailing spaces by treating any sequence of whitespace
        # as a single delimiter and discarding empty strings.
        words = s.split()
        
        # Step 2: Reverse the list of words.
        # words.reverse() modifies the list in-place.
        # Alternatively, one could use `words = words[::-1]` to create a new reversed list.
        words.reverse()
        
        # Step 3: Join the reversed words back into a single string,
        # using a single space as the separator.
        return " ".join(words)