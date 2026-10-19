class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # We need two maps to ensure a one-to-one correspondence:
        # 1. s_to_t: maps characters from string s to characters from string t.
        #    This ensures that all occurrences of a character in s map to the same character in t.
        # 2. t_to_s: maps characters from string t to characters from string s.
        #    This ensures that no two distinct characters in s map to the same character in t
        #    (i.e., a character in t is not mapped from two different characters in s).
        
        s_to_t = {}
        t_to_s = {}

        # The problem statement guarantees s.length == t.length.
        # We iterate through both strings simultaneously using zip.
        for char_s, char_t in zip(s, t):
            # Check the s -> t mapping
            if char_s in s_to_t:
                # If char_s has been mapped before, ensure it maps to the same char_t
                if s_to_t[char_s] != char_t:
                    return False
            else:
                # If char_s is new, establish its mapping to char_t
                s_to_t[char_s] = char_t
            
            # Check the t -> s mapping
            if char_t in t_to_s:
                # If char_t has been mapped from before, ensure it maps from the same char_s
                if t_to_s[char_t] != char_s:
                    return False
            else:
                # If char_t is new, establish its mapping from char_s
                t_to_s[char_t] = char_s
        
        # If we complete the loop without any conflicts, the strings are isomorphic.
        return True