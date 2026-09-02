class Solution:
    def thousandSeparator(self, n: int) -> str:
        s_n = str(n)
        
        result_chars = []
        digit_count = 0
        
        # Iterate through the string representation of the number from right to left.
        # We use enumerate to get both the index (from the right) and the character.
        # The index `i` helps us determine if we are at the leftmost digit of the original string,
        # to avoid adding a dot after it.
        for i, char in enumerate(reversed(s_n)):
            result_chars.append(char)
            digit_count += 1
            
            # If 3 digits have been processed and there are still more digits
            # to the left (i.e., not the last character encountered from the right,
            # which corresponds to the leftmost digit of the original string),
            # append a dot and reset the digit counter.
            if digit_count == 3 and i < len(s_n) - 1:
                result_chars.append('.')
                digit_count = 0
                
        # The `result_chars` list was built in reverse order.
        # Reverse it again to get the correct order and then join the characters
        # to form the final string.
        return "".join(reversed(result_chars))