import collections

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        
        # Use a dictionary to store reserved seats for each row.
        # Key: row number
        # Value: a bitmask representing reserved seats in that row.
        # Seat s (from 2 to 9) maps to bit (s-2).
        # So seat 2 -> bit 0, seat 3 -> bit 1, ..., seat 9 -> bit 7.
        # Seats 1 and 10 are not part of any of the three possible blocks (2-5, 4-7, 6-9), 
        # so reservations in seats 1 or 10 do not affect family placement and can be ignored.
        reserved_row_masks = collections.defaultdict(int)
        
        for r, s in reservedSeats:
            if 2 <= s <= 9:  # Only seats 2-9 are relevant for family blocks
                # Set the corresponding bit for the reserved seat
                reserved_row_masks[r] |= (1 << (s - 2))
        
        # Calculate families for rows with no relevant reservations.
        # Each such row can accommodate 2 families (one in seats 2-5, another in 6-9)
        # because these two blocks (L and R) are disjoint.
        total_families = (n - len(reserved_row_masks)) * 2
        
        # Define bitmasks for the three possible four-person family blocks
        # The seat mapping is: seat s -> bit (s-2)
        # Block L: seats 2,3,4,5 corresponds to bits 0,1,2,3 (binary 00001111)
        MASK_L = 0b00001111  # Decimal 15
        # Block M: seats 4,5,6,7 corresponds to bits 2,3,4,5 (binary 00111100)
        MASK_M = 0b00111100  # Decimal 60
        # Block R: seats 6,7,8,9 corresponds to bits 4,5,6,7 (binary 11110000)
        MASK_R = 0b11110000  # Decimal 240
        
        # Iterate through rows that have at least one reserved seat relevant to the blocks
        for row_mask in reserved_row_masks.values():
            
            families_in_this_row = 0
            
            # Check availability of each block.
            # A block is available if no seat within its mask is reserved,
            # which means (row_mask bitwise-AND block_mask) must be 0.
            is_L_available = (row_mask & MASK_L) == 0
            is_M_available = (row_mask & MASK_M) == 0
            is_R_available = (row_mask & MASK_R) == 0
            
            # Maximize families in this row:
            # The optimal strategy is to prioritize placing two families if possible.
            # Case 1: If both L and R blocks are available, we can place 2 families.
            #         These two blocks (L: seats 2-5 and R: seats 6-9) are disjoint.
            #         This is the maximum possible for any row.
            if is_L_available and is_R_available:
                families_in_this_row = 2
            # Case 2: Otherwise (if we cannot place 2 families), we try to place 1 family.
            #         If any of the three blocks (L, M, or R) are available, we can place 1 family.
            #         Note that if L and R were both available, we would have entered the first 'if'.
            #         So this 'elif' branch covers scenarios where we can only pick one block
            #         (e.g., L is available but R is not, or only M is available, etc.).
            elif is_L_available or is_R_available or is_M_available:
                families_in_this_row = 1
            # Case 3: If none of L, M, or R are available, families_in_this_row remains 0.
            
            total_families += families_in_this_row
            
        return total_families