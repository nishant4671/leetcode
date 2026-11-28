import random

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
        self.radius_sq = radius * radius

    def randPoint(self) -> list[float]:
        while True:
            # Generate random x and y coordinates within the square bounding the circle
            # The range for x and y offsets from the center is [-radius, radius]
            x_offset = random.uniform(-self.radius, self.radius)
            y_offset = random.uniform(-self.radius, self.radius)

            # Check if the generated point (x_offset, y_offset) is inside the circle
            # A point (x, y) is inside a circle of radius R centered at (0,0) if x^2 + y^2 <= R^2
            if x_offset * x_offset + y_offset * y_offset <= self.radius_sq:
                # If it is inside, return the point, shifted by the circle's center
                return [self.x_center + x_offset, self.y_center + y_offset]
            # If the point is outside the circle (in the corners of the bounding square),
            # the loop continues to generate new random coordinates.