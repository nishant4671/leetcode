class Solution:
    def reverseDegree(self, s: str) -> int:
        total_reverse_degree = 0
        ord_a = ord('a')
        
        for i, char in enumerate(s):
            # Calculate the 0-indexed position of the character in the standard alphabet.
            # 'a' -> 0, 'b' -> 1, ..., 'z' -> 25
            std_alpha_pos = ord(char) - ord_a
            
            # Calculate the position in the reversed alphabet.
            # 'a' -> 26, 'b' -> 25, ..., 'z' -> 1
            reversed_alpha_value = 26 - std_alpha_pos
            
            # Calculate the 1-indexed position of the character in the string.
            # First character (index 0) -> 1, second character (index 1) -> 2, etc.
            string_pos_1_indexed = i + 1
            
            # Add the product of these two values to the total sum.
            total_reverse_degree += reversed_alpha_value * string_pos_1_indexed
            
        return total_reverse_degree