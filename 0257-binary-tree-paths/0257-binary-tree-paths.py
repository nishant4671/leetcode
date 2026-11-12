# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        
        all_paths = []

        def dfs(node, current_path_values):
            # Add the current node's value (as a string) to the path list
            current_path_values.append(str(node.val))

            # If the current node is a leaf node
            if not node.left and not node.right:
                # Form the path string by joining values with "->" and add to results
                all_paths.append("->".join(current_path_values))
            else:
                # If not a leaf, recurse on children if they exist
                if node.left:
                    dfs(node.left, current_path_values)
                if node.right:
                    dfs(node.right, current_path_values)
            
            # Backtrack: remove the current node's value from the path list
            # This allows exploration of other branches without interference
            current_path_values.pop()

        # The problem constraints guarantee root is not None (number of nodes is [1, 100]).
        # Start the DFS traversal from the root with an empty path list.
        dfs(root, [])
        return all_paths