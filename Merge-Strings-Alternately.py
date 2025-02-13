'''

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d

https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged=[] # Created a list to store the output string, We didn't create a string, as they are immutable and cannot use append
        i = 0 # iterable variable
        while i < len(word1) or i < len(word2): # condition check
            if i < len(word1): # If i is less than length of word1
                merged.append(word1[i]) # Append its element to merged
            if i < len(word2): # If i is less than length of word2 
                merged.append(word2[i]) # Append its element to merged
            i += 1 # Increment value of i for each iteration
        return ''.join(merged) # Since we need to return a string, join the list to empty string and return a string

        # O(n) - Time complexcity as we are iterating over the strings.
        
