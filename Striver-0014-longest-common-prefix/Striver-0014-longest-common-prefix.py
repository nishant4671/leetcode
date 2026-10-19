class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # According to constraints: 1 <= strs.length <= 200.
        # This means `strs` will always have at least one element,
        # so `strs[0]` is safe to access.

        # Take the first string as our primary reference for comparison.
        first_str = strs[0]
        
        # If the first string itself is empty, then no common prefix can exist,
        # so the longest common prefix must be an empty string.
        # This handles cases like strs = ["", "abc", "abd"].
        if not first_str:
            return ""

        # Iterate through each character of the `first_str`.
        # The index `i` represents the potential length of the LCP being checked.
        for i in range(len(first_str)):
            char_to_match = first_str[i]
            
            # For each character `char_to_match` from `first_str`,
            # compare it with the character at the same position `i`
            # in all other strings in the list.
            # We start from the second string (index 1) up to the end of the list.
            for j in range(1, len(strs)):
                current_str = strs[j]
                
                # We stop and return the common prefix found so far if either:
                # 1. The `current_str` is shorter than the current index `i`.
                #    This means `current_str` does not have a character at position `i`,
                #    so the common prefix cannot extend to this point.
                # 2. The character at `current_str[i]` does not match `char_to_match`.
                #    This indicates a mismatch, and the commonality breaks.
                if i >= len(current_str) or current_str[i] != char_to_match:
                    # If either condition is met, the common prefix ends before or at this character.
                    # We return the substring of `first_str` from its beginning (index 0)
                    # up to (but not including) the current index `i`.
                    return first_str[0:i]
        
        # If the outer loop completes without returning, it means all characters
        # of `first_str` have been successfully matched in all other strings.
        # In this scenario, `first_str` itself is the longest common prefix.
        return first_str