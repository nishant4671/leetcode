class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        results = []
        current_combination = []

        def backtrack(open_count, close_count):
            if open_count == n and close_count == n:
                results.append("".join(current_combination))
                return

            if open_count < n:
                current_combination.append("(")
                backtrack(open_count + 1, close_count)
                current_combination.pop()

            if close_count < open_count:
                current_combination.append(")")
                backtrack(open_count, close_count + 1)
                current_combination.pop()

        backtrack(0, 0)
        return results