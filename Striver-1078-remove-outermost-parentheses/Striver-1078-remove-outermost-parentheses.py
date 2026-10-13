class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # result_chars will store the characters of the modified string.
        # Using a list for character accumulation is efficient in Python.
        result_chars = []
        
        # 'balance' tracks the current nesting level of parentheses.
        # It increments for '(' and decrements for ')'.
        # A primitive string starts when balance is 0 and we see '(',
        # and ends when balance returns to 0 after seeing ')'.
        balance = 0
        
        for char in s:
            if char == '(':
                # When an opening parenthesis is encountered:
                # If balance is already greater than 0, it means this '(' is not
                # the very first opening parenthesis of a new primitive string.
                # It's an inner parenthesis that should be kept.
                if balance > 0:
                    result_chars.append(char)
                # Always increment balance for an opening parenthesis.
                balance += 1
            else: # char == ')'
                # When a closing parenthesis is encountered:
                # Always decrement balance for a closing parenthesis first.
                balance -= 1
                # If balance is still greater than 0 after decrementing, it means
                # this ')' is not the outermost closing parenthesis of the current
                # primitive string. It's an inner parenthesis that should be kept.
                if balance > 0:
                    result_chars.append(char)
        
        # Join the list of characters to form the final result string.
        return "".join(result_chars)