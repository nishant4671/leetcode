class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        words = sentence.split(' ')
        
        transformed_words = []
        
        for i, word in enumerate(words):
            word_index = i + 1 
            
            first_char = word[0]
            
            current_transformed_word = ""
            
            if first_char in vowels:
                current_transformed_word = word + "ma"
            else:
                current_transformed_word = word[1:] + first_char + "ma"
            
            current_transformed_word += 'a' * word_index
            
            transformed_words.append(current_transformed_word)
            
        return " ".join(transformed_words)