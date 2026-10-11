class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        max_len = 0
        current_len = 0
        vowels_set = set()
        prev_char = ' ' # Use a character lexicographically smaller than 'a' for initial comparison

        for char in word:
            curr_char = char

            if curr_char < prev_char:
                # Order is broken. Reset the current substring state.
                current_len = 0
                vowels_set.clear()
            
            # Now, process `curr_char` based on its value and current state.
            if curr_char == 'a':
                if current_len == 0:
                    # Brand new start of a candidate substring
                    current_len = 1
                    vowels_set = {'a'}
                elif prev_char == 'a': 
                    # Continuing an 'a' sequence
                    current_len += 1
                # If current_len > 0 and prev_char != 'a' (e.g., 'i' then 'a'),
                # `curr_char < prev_char` would have already reset current_len to 0,
                # leading to the `current_len == 0` case above.
            elif current_len > 0 and curr_char >= prev_char:
                # Continue extending the current beautiful substring candidate.
                # `current_len > 0` ensures we are actively building a sequence that started with 'a'.
                # `curr_char >= prev_char` ensures alphabetical order.
                current_len += 1
                vowels_set.add(curr_char)
            else:
                # This `else` branch handles cases where:
                # 1. `current_len` is 0 and `curr_char` is not 'a' (cannot start a beautiful substring).
                # 2. `current_len > 0` but `curr_char < prev_char` (already caught by the first `if` and reset).
                # In essence, this state means we're not building a valid substring.
                current_len = 0
                vowels_set.clear()

            # Check if the current candidate substring is beautiful
            # Only update max_len if we have collected all 5 distinct vowels.
            if len(vowels_set) == 5:
                max_len = max(max_len, current_len)
            
            prev_char = curr_char
            
        return max_len