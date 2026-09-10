# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count_matching_nodes = 0

        # Helper function performs a post-order traversal.
        # For each node, it calculates the sum of values and the count of nodes in its subtree.
        # It updates self.count_matching_nodes if the node's value equals its subtree's average.
        # Returns a tuple: (sum of subtree values, count of nodes in subtree).
        def dfs(node):
            if not node:
                # Base case: An empty tree has a sum of 0 and a count of 0 nodes.
                return 0, 0

            # Recursively get the sum and count for the left subtree.
            left_sum, left_count = dfs(node.left)
            
            # Recursively get the sum and count for the right subtree.
            right_sum, right_count = dfs(node.right)

            # Calculate the total sum and total count for the current node's subtree.
            # This includes the current node's value and 1 for the current node itself.
            current_subtree_sum = node.val + left_sum + right_sum
            current_subtree_count = 1 + left_count + right_count

            # Calculate the average for the current subtree, rounded down.
            # current_subtree_count will always be at least 1 (for the current node itself),
            # so division by zero is not a concern.
            average = current_subtree_sum // current_subtree_count

            # If the current node's value equals the calculated average, increment the counter.
            if node.val == average:
                self.count_matching_nodes += 1
            
            # Return the sum and count of the current subtree to its parent.
            return current_subtree_sum, current_subtree_count
        
        # Start the DFS traversal from the root of the tree.
        dfs(root)
        
        # After the traversal, self.count_matching_nodes holds the total count
        # of nodes whose values match their subtree averages.
        return self.count_matching_nodes