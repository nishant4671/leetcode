
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

class Solution(object):
    def letterCombinations(self, digits):
        from itertools import product #this is to get the cartesian product of the list of letters corresponding to the digits provided in the input string called digits
        numbers = [int(char) for char in digits]
        print("the numbers present in the string are", numbers)#this here is to extract all the individual numbers from the provided string called digits


        data = {  #this is the mapping of the numbers to the letters as per the telephone keypad 

            "2" : ["a", "b" , "c"]
            , "3" : ["d", "e" , "f"]
            , "4" : ["g", "h" , "i"]
            , "5" : ["j", "k" , "l"]
            , "6" : ["m", "n" , "o"]
            , "7" : ["p", "q" , "r", "s"]
            , "8" : ["t", "u" , "v"]
            , "9" : ["w", "x" , "y", "z"]



        }

        selected_letters =[data[key] for key in digits] 
        combinations = list(product(*selected_letters))#this is to get the cartesian product of the list of the letters corresponding to the digits provided in the input string called digits
        #this is returning in the form of a list of tuples where each tuple cnatins a combination of letters corresponding to the digits provided in the input string 
        #however we need to convert each tuple into a sring and then return the list of string as the final output 
        #this is how we do it 
        result = ["".join(combination) for combination in combinations] #this is to convert each tuple into a string and then return the list of string as the final output
        #the join method is used to concatenate the elements of the tuple into a single string and then we are using a list comprehension to create a list of strings from the list of tuples



        return result