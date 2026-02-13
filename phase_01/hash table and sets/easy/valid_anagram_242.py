# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

#  what is an anagram? An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution(object):
    def isAnangram(self, s, t):
        if len(s)!=len(t):
            return False
        count_of_s = {}# this here means that we will create an empty dictionary called count_of_s to store the count of each letter in the string s
        count_of_y = {}# this here means that we will create an empty dictionary called count_of_y to store the count of each letter in the string t
        for i in range(len(s)):
            if s[i] in count_of_s:
                count_of_s[s[i]]+=1 #this here means that if the letter is already in the count_of_s dictioanry, then we will add 1 to the count of that letter in the dictionary
            else:
                count_of_s[s[i]]=1 #this here means that if the letter is not in the dictionary , then we will add the letter to the dictioanry and add 1 to its count in the dictionary 

            if t[i] in count_of_y:
                count_of_y[t[i]]+=1 # this here means that if the letter is already in the count_of_y dictioanry, then we will add 1 to the count of that letter in the dictionary
            else:
                count_of_y[t[i]]=1 # this here means that if the letter is not in the dictionary , then we will add the letter to the dictioanry and add 1 to its count in the dictionary

            if count_of_s!=count_of_y:# this here means that if the count of letters in the count_of_s dictionary is not equal to the count of letters in the count_of_y dictionary, then we will return false because it means that the two strings are not anagrams of each other
                return false 