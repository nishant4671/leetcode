class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        list_A = []
        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    list_A.append((r, c))
        
        list_B = []
        for r in range(n):
            for c in range(n):
                if img2[r][c] == 1:
                    list_B.append((r, c))
        
        overlap_counts = collections.defaultdict(int)
        
        max_overlap = 0
        
        for r_a, c_a in list_A:
            for r_b, c_b in list_B:
                dr = r_a - r_b
                dc = c_a - c_b
                
                overlap_counts[(dr, dc)] += 1
                
                max_overlap = max(max_overlap, overlap_counts[(dr, dc)])
                
        return max_overlap