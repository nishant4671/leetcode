import collections
from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        # Build the initial adjacency list for the tree.
        # adj[u] will contain all children of node u in the original tree.
        adj = collections.defaultdict(list)
        for i in range(1, n):
            adj[parent[i]].append(i)

        # This array will store the new parent for each node in the final tree.
        # new_parents[i] will be the parent of node i after changes.
        # Node 0 is the root and will conceptually have -1 as its parent.
        new_parents = [0] * n 
        new_parents[0] = -1 

        # last_occurrence[char_code] stores the closest ancestor (node index)
        # encountered so far in the current DFS path that has the character
        # corresponding to 'a' + char_code.
        # Initialize with -1 to indicate no such ancestor found yet for any character.
        last_occurrence = [-1] * 26 

        # DFS function to determine the new parent for each node.
        # It traverses the original tree structure.
        def dfs_find_new_parents(u):
            char_code_u = ord(s[u]) - ord('a')
            
            # Store the current value of last_occurrence[char_code_u] to restore it later.
            # This is crucial for correct backtracking when returning from recursion,
            # ensuring that 'u' is only considered an ancestor while its subtree is active.
            prev_u_char_ancestor = last_occurrence[char_code_u]
            
            # Update last_occurrence for char_code_u to the current node u.
            # This makes 'u' the most recent ancestor for its character on the current path.
            last_occurrence[char_code_u] = u

            # Iterate over children of u in the original tree.
            for v in adj[u]:
                char_code_v = ord(s[v]) - ord('a')
                
                # Check if an ancestor with the same character as v exists on the path from root to u.
                target_ancestor = last_occurrence[char_code_v]

                if target_ancestor != -1:
                    # If such an ancestor 'y' exists, it becomes the new parent of 'v'.
                    # This 'target_ancestor' is guaranteed to be the *closest* ancestor
                    # because last_occurrence is updated greedily during the DFS traversal.
                    new_parents[v] = target_ancestor
                else:
                    # If no ancestor with the same character is found,
                    # the original parent (u) remains the parent of v.
                    new_parents[v] = u
                
                # Recursively call DFS for the child v to determine its new parent and its children's parents.
                dfs_find_new_parents(v)
            
            # Backtrack: Restore last_occurrence[char_code_u] to its state
            # before processing node u. This removes 'u' from being an active ancestor
            # for its character once its subtree has been fully processed.
            last_occurrence[char_code_u] = prev_u_char_ancestor

        # Start the DFS from the root (node 0) to determine all new parents based on the original tree.
        dfs_find_new_parents(0)

        # Build the final adjacency list based on the new_parents array.
        # final_adj[u] will contain all children of node u in the final tree.
        final_adj = collections.defaultdict(list)
        for i in range(1, n):
            final_adj[new_parents[i]].append(i)

        # Initialize the answer array to store subtree sizes.
        answer = [0] * n

        # DFS function to calculate subtree sizes in the final tree.
        def dfs_subtree_size(u):
            current_subtree_size = 1 # Node u itself contributes 1 to its subtree size
            # Recursively sum up sizes of subtrees rooted at its children in the final tree.
            for v in final_adj[u]:
                current_subtree_size += dfs_subtree_size(v)
            
            # Store the calculated subtree size for node u.
            answer[u] = current_subtree_size
            return current_subtree_size
        
        # Start the DFS from the root (node 0) to calculate all subtree sizes in the final tree.
        dfs_subtree_size(0)

        return answer