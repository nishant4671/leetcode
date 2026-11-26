class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        
        n = len(s1)
        
        # Convert strings to lists of characters and sort them.
        # Sorting is crucial because to determine if one string can "break" another
        # through *any* permutation, it is optimal to sort both strings.
        # If the sorted characters satisfy the condition, then the original strings
        # can form permutations that satisfy the condition.
        # Conversely, if no permutations can satisfy the condition, then the sorted
        # versions also cannot satisfy it.
        s1_sorted = sorted(s1)
        s2_sorted = sorted(s2)
        
        # Helper function to check if one sorted list of characters (x_sorted)
        # can "break" another (y_sorted).
        # This means checking if x_sorted[i] >= y_sorted[i] for all indices i.
        def check_break_condition(x_sorted: list[str], y_sorted: list[str]) -> bool:
            for i in range(n):
                if x_sorted[i] < y_sorted[i]:
                    return False # Condition x[i] >= y[i] is violated for this index
            return True # Condition holds for all characters
        
        # The problem asks if a permutation of s1 can break a permutation of s2
        # OR if a permutation of s2 can break a permutation of s1.
        # We check both possibilities using our sorted character lists.
        can_s1_break_s2 = check_break_condition(s1_sorted, s2_sorted)
        can_s2_break_s1 = check_break_condition(s2_sorted, s1_sorted)
        
        return can_s1_break_s2 or can_s2_break_s1