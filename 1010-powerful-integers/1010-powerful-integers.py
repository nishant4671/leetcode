from typing import List

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        powerful_integers = set()

        # Iterate through powers of x (x^i)
        px = 1 # Represents x^0 initially
        while px <= bound:
            # Iterate through powers of y (y^j)
            py = 1 # Represents y^0 initially
            while px + py <= bound:
                powerful_integers.add(px + py)

                # If y is 1, y^j will always be 1. Multiplying by y won't change py.
                # To avoid an infinite loop and duplicate calculations, break after the first iteration (j=0).
                if y == 1:
                    break
                py *= y # Calculate the next power of y

            # If x is 1, x^i will always be 1. Multiplying by x won't change px.
            # To avoid an infinite loop and duplicate calculations, break after the first iteration (i=0).
            if x == 1:
                break
            px *= x # Calculate the next power of x

        return list(powerful_integers)