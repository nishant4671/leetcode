class Solution:
    def minInsertions(self, s: str) -> int:
        open_needed = 0  # Represents the number of currently open '(' that still need to be balanced by '))'
        insertions = 0   # Total insertions required

        i = 0
        n = len(s)
        while i < n:
            if s[i] == '(':
                # When an opening parenthesis is encountered, it needs a '))' to balance.
                open_needed += 1
                i += 1
            else:  # s[i] == ')'
                # This is a right parenthesis. It could be part of a ')).' pair.
                
                # Check if s[i] is immediately followed by another ')'
                if i + 1 < n and s[i+1] == ')':
                    # We found a ')).' pair.
                    if open_needed > 0:
                        # There's an open '(' that this ')).' can close.
                        open_needed -= 1
                    else:
                        # No open '(' to close. We must insert an opening '('.
                        insertions += 1
                    # Consume both ')' characters.
                    i += 2
                else:
                    # We found a single ')'. It needs another ')' to form a ')).'
                    insertions += 1  # Insert one ')'
                    
                    if open_needed > 0:
                        # This single ')' (plus the one we just inserted) forms a ')).'
                        # which can close an existing '('.
                        open_needed -= 1
                    else:
                        # No open '(' to close. We need to insert an opening '('
                        # to match this conceptual ')).' pair.
                        insertions += 1
                    # Consume the current ')' character.
                    i += 1

        # After iterating through the string, any remaining 'open_needed'
        # means we have unclosed '(' parentheses.
        # Each remaining '(' needs a ')).' to balance it.
        # This means 2 ')' characters per remaining '('.
        insertions += open_needed * 2

        return insertions