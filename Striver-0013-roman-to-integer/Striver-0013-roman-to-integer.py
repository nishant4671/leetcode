class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        n = len(s)

        # Iterate through the Roman numeral string from left to right
        for i in range(n):
            current_value = roman_map[s[i]]
            
            # Check if there is a next character and if the current symbol's value
            # is less than the next symbol's value.
            # This indicates a subtractive case (e.g., IV, IX, XL, etc.).
            if i + 1 < n and current_value < roman_map[s[i+1]]:
                # If it's a subtractive case, subtract the current value.
                # The next character's value will be added in the next iteration.
                total -= current_value
            else:
                # Otherwise (current value is greater than or equal to the next,
                # or it's the last character), add the current value.
                total += current_value
                
        return total