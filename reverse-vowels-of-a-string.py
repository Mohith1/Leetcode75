'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

https://leetcode.com/problems/reverse-vowels-of-a-string



class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u','A','E','I','O','U'} #Stored in a set
        present_vowels = [] #To store the vowels present in a string
        s = list(s) #Convert string to list to iterate better
        for i in range(len(s)):
            if s[i] in vowels:
                present_vowels.append(s[i]) #Append the vowels present in the current string
        present_vowels.reverse() #Reverse them using .reverse() command
        index = 0
        for i in range(len(s)):
            if s[i] in vowels: #Run a for loop again and swap the values
                s[i] = present_vowels[index] #Make sure the index is independent #from loop variable
                index +=1
        return ''.join(s) # Join to form the output string

        
