class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        # Initialize parent array for 26 lowercase letters ('a' through 'z')
        # Each letter is initially its own parent, representing a distinct set.
        parent = list(range(26))

        # Helper function to find the root of an element (with path compression)
        def find(i):
            if parent[i] == i:
                return i
            # Path compression: make the current node directly point to its root
            parent[i] = find(parent[i])
            return parent[i]

        # Helper function to union two sets
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                # Merge the set of i into the set of j (or vice versa)
                parent[root_i] = root_j
                return True # Sets were merged
            return False # Elements were already in the same set

        # First pass: Process all equality equations ("x==y")
        # If x == y, then x and y must belong to the same equivalence class.
        # We use union-find to merge their sets.
        for eq_str in equations:
            op = eq_str[1:3]
            if op == "==":
                var1_char = eq_str[0]
                var2_char = eq_str[3]

                # Convert characters to 0-indexed integers ('a' -> 0, 'b' -> 1, ...)
                var1_idx = ord(var1_char) - ord('a')
                var2_idx = ord(var2_char) - ord('a')

                union(var1_idx, var2_idx)

        # Second pass: Process all inequality equations ("x!=y")
        # If x != y, then x and y must belong to different equivalence classes.
        # We check if they are currently in the same set according to our
        # union-find structure. If they are, it's a contradiction, and the
        # equations cannot be satisfied.
        for eq_str in equations:
            op = eq_str[1:3]
            if op == "!=":
                var1_char = eq_str[0]
                var2_char = eq_str[3]

                var1_idx = ord(var1_char) - ord('a')
                var2_idx = ord(var2_char) - ord('a')

                # If the roots are the same, it means var1_idx and var2_idx are
                # considered equal by the "==" operations, which contradicts "!==".
                if find(var1_idx) == find(var2_idx):
                    return False # Contradiction found

        # If we complete both passes without finding any contradictions,
        # then it is possible to satisfy all equations.
        return True