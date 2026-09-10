class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Initialize parent array for 26 lowercase English letters ('a' through 'z').
        # Each character is initially its own parent, meaning it's in its own set.
        # parent[i] stores the representative (root) of the set that character 'a' + i belongs to.
        parent = list(range(26))

        # The find operation with path compression.
        # It returns the representative of the set containing character 'a' + i.
        # This representative will be the lexicographically smallest character in its equivalence class
        # due to the merging strategy in the union operation.
        def find(i):
            if parent[i] == i:
                return i
            # Path compression: make every node on the path point directly to the root
            parent[i] = find(parent[i])
            return parent[i]

        # The union operation.
        # Merges the sets containing character 'a' + i and 'a' + j.
        # The root of the merged set will be the lexicographically smaller of the two original roots.
        def union(i, j):
            root_i = find(i)
            root_j = find(j)

            if root_i != root_j:
                # To ensure the representative of the combined set is always the lexicographically
                # smallest character, the larger root always points to the smaller root.
                if root_i < root_j:
                    parent[root_j] = root_i
                else:
                    parent[root_i] = root_j

        # Process s1 and s2 to establish all equivalences based on the given pairs.
        # For each corresponding pair (s1[k], s2[k]), the characters are considered equivalent.
        for k in range(len(s1)):
            char1_code = ord(s1[k]) - ord('a')
            char2_code = ord(s2[k]) - ord('a')
            union(char1_code, char2_code)
        
        # Build the result string by replacing each character in baseStr with its
        # lexicographically smallest equivalent character.
        result_chars = []
        for char_c in baseStr:
            char_code = ord(char_c) - ord('a')
            # Find the root (smallest equivalent character's code) for the current character
            smallest_equivalent_code = find(char_code)
            # Convert the code back to a character and append to the result
            result_chars.append(chr(smallest_equivalent_code + ord('a')))
            
        return "".join(result_chars)