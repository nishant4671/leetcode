class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knowledge_map = {key: value for key, value in knowledge}
        
        result_parts = []
        current_key_chars = []
        in_bracket = False
        
        for char in s:
            if char == '(':
                in_bracket = True
                current_key_chars = []
            elif char == ')':
                in_bracket = False
                key_str = "".join(current_key_chars)
                value = knowledge_map.get(key_str, "?")
                result_parts.append(value)
            else:
                if in_bracket:
                    current_key_chars.append(char)
                else:
                    result_parts.append(char)
                    
        return "".join(result_parts)