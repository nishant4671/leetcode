class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = 0  # Minimum possible count of unmatched open parentheses
        max_open = 0  # Maximum possible count of unmatched open parentheses

        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                # A ')' must close an open parenthesis.
                # It reduces both the minimum and maximum possible open counts.
                min_open -= 1
                max_open -= 1
            else:  # char == '*'
                # A '*' can be treated as ')' to reduce the minimum count of required open parentheses.
                # If min_open is already 0, treating '*' as ')' would make it -1.
                # However, min_open cannot be truly negative, as '*' can also be an empty string
                # to avoid a deficit. So, we cap it at 0.
                min_open -= 1
                # A '*' can be treated as '(' to increase the maximum count of available open parentheses.
                max_open += 1
            
            # min_open cannot go below zero. If it attempts to, it means we've
            # encountered a ')' or treated a '*' as ')' when there were no
            # guaranteed open parentheses. We can 'absorb' this by treating a
            # prior '*' as empty or '('. So, min_open is capped at 0.
            min_open = max(0, min_open)
            
            # If max_open ever becomes negative, it means we have encountered too many ')'
            # that cannot be matched, even if all '*' were treated as '('.
            # In this case, the string is definitely invalid.
            if max_open < 0:
                return False
        
        # After iterating through the entire string, for it to be valid,
        # the minimum possible count of unmatched open parentheses must be 0.
        # This ensures that all open parentheses can be matched. If min_open > 0,
        # it means there's no way to match all opening parentheses.
        return min_open == 0