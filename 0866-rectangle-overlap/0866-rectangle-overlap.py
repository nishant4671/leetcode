class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1_1, y1_1, x2_1, y2_1 = rec1
        x1_2, y1_2, x2_2, y2_2 = rec2
        
        # Check for overlap on the X-axis
        # An overlap exists if rec1's left edge is to the left of rec2's right edge AND
        # rec2's left edge is to the left of rec1's right edge.
        # This means the intervals (x1_1, x2_1) and (x1_2, x2_2) must strictly intersect.
        x_overlap = x1_1 < x2_2 and x1_2 < x2_1

        # Check for overlap on the Y-axis
        # An overlap exists if rec1's bottom edge is below rec2's top edge AND
        # rec2's bottom edge is below rec1's top edge.
        # This means the intervals (y1_1, y2_1) and (y1_2, y2_2) must strictly intersect.
        y_overlap = y1_1 < y2_2 and y1_2 < y2_1

        # Rectangles overlap if and only if they overlap on both X and Y axes.
        return x_overlap and y_overlap