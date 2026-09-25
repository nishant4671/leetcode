import collections

class LockingTree:

    def __init__(self, parent: list[int]):
        n = len(parent)
        self.parent = parent
        # locked_by[i] stores the user_id if node i is locked, 0 otherwise (unlocked).
        # User IDs are 1 <= user <= 10^4, so 0 is a safe value for unlocked status.
        self.locked_by = [0] * n  
        
        # Build children adjacency list for efficient descendant lookup
        # children[i] will contain a list of direct children of node i.
        self.children = [[] for _ in range(n)]
        # Node 0 is the root and parent[0] == -1, so we start from node 1.
        for i in range(1, n):
            self.children[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        # A node can only be locked if it is currently unlocked.
        if self.locked_by[num] == 0:
            self.locked_by[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        # A node can only be unlocked if it is currently locked by the same user.
        if self.locked_by[num] == user:
            self.locked_by[num] = 0
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        # Condition 1: The node must be unlocked.
        if self.locked_by[num] != 0:
            return False

        # Condition 3: It must not have any locked ancestors.
        curr_ancestor = self.parent[num]
        while curr_ancestor != -1:
            if self.locked_by[curr_ancestor] != 0: # If ancestor is locked
                return False
            curr_ancestor = self.parent[curr_ancestor]

        # Condition 2: It must have at least one locked descendant (by any user).
        # We also collect all descendants to unlock them later if the upgrade is successful.
        has_locked_descendant = False
        descendants_to_unlock = []
        
        # Use a queue for Breadth-First Search (BFS) to find all descendants.
        # Start BFS from the direct children of 'num'.
        q_for_descendants = collections.deque()
        for child in self.children[num]:
            q_for_descendants.append(child)
        
        while q_for_descendants:
            curr_node = q_for_descendants.popleft()
            
            # Check if this descendant is locked
            if self.locked_by[curr_node] != 0:
                has_locked_descendant = True
            
            # Add this node to the list of descendants to potentially unlock
            descendants_to_unlock.append(curr_node) 
            
            # Add children of the current node to the queue for further traversal
            for child_of_curr in self.children[curr_node]:
                q_for_descendants.append(child_of_curr)
                
        # If no locked descendant was found, Condition 2 is not met.
        if not has_locked_descendant:
            return False
            
        # If all three conditions are met, perform the upgrade actions:
        # 1. Lock node 'num' for the given user.
        self.locked_by[num] = user
        
        # 2. Unlock all its descendants (regardless of who locked them).
        for descendant in descendants_to_unlock:
            self.locked_by[descendant] = 0
            
        return True