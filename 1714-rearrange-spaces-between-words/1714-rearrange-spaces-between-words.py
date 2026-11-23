class Solution:
    def reorderSpaces(self, text: str) -> str:
        total_spaces = text.count(' ')
        words = text.split()
        num_words = len(words)

        if num_words == 1:
            spaces_per_gap = 0
            extra_spaces = total_spaces
        else:
            spaces_per_gap = total_spaces // (num_words - 1)
            extra_spaces = total_spaces % (num_words - 1)
        
        space_separator = ' ' * spaces_per_gap
        
        result = space_separator.join(words)
        
        result += ' ' * extra_spaces
        
        return result