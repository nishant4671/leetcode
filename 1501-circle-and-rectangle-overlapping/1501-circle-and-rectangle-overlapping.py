class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        
        # Find the coordinates of the closest point in the rectangle to the circle's center.
        
        # Clamp xCenter to the rectangle's x-range [x1, x2]
        closestX = max(x1, min(xCenter, x2))
        
        # Clamp yCenter to the rectangle's y-range [y1, y2]
        closestY = max(y1, min(yCenter, y2))
        
        # Calculate the squared distance between the circle's center and this closest point.
        distX = xCenter - closestX
        distY = yCenter - closestY
        
        # squared distance
        dist_sq = distX * distX + distY * distY
        
        # Check if this squared distance is less than or equal to the squared radius.
        # If it is, the circle overlaps with the rectangle.
        return dist_sq <= radius * radius