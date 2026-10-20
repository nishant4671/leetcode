class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Step 1: Check if the lengths of the two strings are equal.
        # If they are not equal, 's' cannot be rotated to form 'goal'.
        if len(s) != len(goal):
            return False
        
        # Step 2: Handle the edge case of empty strings.
        # According to constraints, s.length and goal.length are at least 1,
        # so this specific check might not be strictly necessary, but good practice.
        # If both are empty, they are equal and considered a rotation of each other.
        if not s: # This implies both s and goal are empty due to the length check above.
            return True

        # Step 3: Concatenate 's' with itself.
        # Any string that is a rotation of 's' must be a substring of 's' + 's'.
        # For example, if s = "abcde", then s + s = "abcdeabcde".
        # All rotations like "bcdea", "cdeab", etc., are present within "abcdeabcde".
        s_double = s + s
        
        # Step 4: Check if 'goal' is a substring of 's_double'.
        # Python's 'in' operator for strings efficiently performs this substring check.
        return goal in s_double