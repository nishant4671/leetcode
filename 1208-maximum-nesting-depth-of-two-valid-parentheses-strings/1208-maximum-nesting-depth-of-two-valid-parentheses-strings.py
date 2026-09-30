class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        depth = 0
        for char in seq:
            if char == '(':
                # Assign this opening parenthesis to group based on its current nesting depth.
                # Then increment depth for subsequent characters.
                ans.append(depth % 2)
                depth += 1
            else:  # char == ')'
                # Decrement depth first, as this closing parenthesis
                # marks the end of the current nesting level.
                # Then assign it to group based on the new, shallower depth.
                depth -= 1
                ans.append(depth % 2)
        return ans