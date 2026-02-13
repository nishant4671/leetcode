# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 



class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        count_of_ransomNote = {} # this here means that we will create an empty dictionary called count_of_ransomNote to store the count of each letter in the string ransomNote
        count_of_madazine = {} # this here means that we will create an empty dictionary called count_of_magazine to store the count of each letter in the string magazine
        for i in range(len(ransomNote)):
            if ransomNote[i] in count_of_ransomNote:
                count_of_ransomNote[ransomNote[i]]+=1 # this here means that if the letter is already in the count_of_ransomNote dictioanry, then we will add 1 to the count of that letter in the dictionary
            else:
                count_of_ransomNote[ransomNote[i]]=1 # this here means that if the letter is not in the dictionary , then we will add the letter to the dictioanry and add 1 to its count in the dictionary



        for i in range(len(magazine)):
            if magazine[i] in count_of_madazine:
                count_of_madazine[magazine[i]]+=1 # this here means that if the letter is already in the count_of_magazine dictioanry, then we will add 1 to the count of that letter in the dictionary
            else:
                count_of_madazine[magazine[i]]=1 # this here means that if the letter is not in the dictionary , then we will add the letter to the dictioanry and add 1 to its count in the dictionary

        for key in count_of_ransomNote:
            if key not in count_of_madazine: # this here means that if the letter in the count_of_ransomNote dictionary is not in the count_of_magazine dictionary, then we will return false because it means that the ransomNote cannot be constructed by using the letters from magazine
                return False
            elif count_of_ransomNote[key]>count_of_madazine[key]: # this here means that if the count of a letter in the count_of_ransomNote dictionary is greater than the count of that letter in the count_of_magazine dictionary, then we will return false because it means that the ransomNote cannot be constructed by using the letters from magazine
                return False
            
        return True # this here means that if we have gone through all the letters in the count_of_ransomNote dictionary and we have not returned false, then we will return true because it means that the ransomNote can be constructed by using the letters from magazine
    
    