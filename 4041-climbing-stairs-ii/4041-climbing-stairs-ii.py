class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # We need to find the minimum cost to reach step 'n'.
        # We start at step 0 with an initial cost of 0.
        # From step i, we can jump to i+1, i+2, or i+3.
        # The cost of a jump from i to j is costs[j] + (j - i)^2.
        # The 'costs' array is 1-indexed, meaning costs[k] in the problem refers to
        # the (k-1)-th element in the Python list 'costs' for k from 1 to n.

        # We can use dynamic programming with O(1) space complexity,
        # as the cost to reach step 'i' only depends on the minimum costs
        # to reach steps 'i-1', 'i-2', and 'i-3'.

        # dp_minus_3 stores the minimum cost to reach step i-3.
        # dp_minus_2 stores the minimum cost to reach step i-2.
        # dp_minus_1 stores the minimum cost to reach step i-1.

        # Initialize base cases for steps before step 1.
        # Step 0 has a cost of 0. Steps less than 0 are considered unreachable
        # and are initialized with infinity.
        import math
        dp_minus_3 = math.inf  # Represents min_cost(step -2) logically for calculating min_cost(step 1)
        dp_minus_2 = math.inf  # Represents min_cost(step -1) logically for calculating min_cost(step 1)
        dp_minus_1 = 0         # Represents min_cost(step 0)

        # Iterate from step 1 up to step n to calculate the minimum cost for each step.
        for i in range(1, n + 1):
            # The base cost of landing on the current step 'i' is costs[i-1]
            # because the input 'costs' array is 0-indexed in Python but
            # represents 1-indexed steps from 1 to n.
            current_step_base_cost = costs[i - 1]

            # Calculate the cost if we jumped from step i-1 to i (a 1-step jump).
            # The jump cost component is (1)^2 = 1.
            option1_cost = dp_minus_1 + current_step_base_cost + 1

            # Calculate the cost if we jumped from step i-2 to i (a 2-step jump).
            # The jump cost component is (2)^2 = 4.
            option2_cost = dp_minus_2 + current_step_base_cost + 4

            # Calculate the cost if we jumped from step i-3 to i (a 3-step jump).
            # The jump cost component is (3)^2 = 9.
            option3_cost = dp_minus_3 + current_step_base_cost + 9

            # The minimum cost to reach the current step 'i' is the minimum of these options.
            dp_current = min(option1_cost, option2_cost, option3_cost)

            # Update the variables for the next iteration (i+1).
            # The cost to reach step i-2 becomes the cost to reach step i-3 for (i+1).
            # The cost to reach step i-1 becomes the cost to reach step i-2 for (i+1).
            # The cost to reach step i (dp_current) becomes the cost to reach step i-1 for (i+1).
            dp_minus_3 = dp_minus_2
            dp_minus_2 = dp_minus_1
            dp_minus_1 = dp_current

        # After the loop completes, dp_minus_1 will hold the minimum cost to reach step n.
        return dp_minus_1