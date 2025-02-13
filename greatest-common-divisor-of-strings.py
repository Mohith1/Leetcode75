'''
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

https://leetcode.com/problems/greatest-common-divisor-of-strings
'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1: # If we have a GCD the concatenated strings must be equal and if they are not then if means We cannot form GCD
            return ""

        def gcd(len1, len2):
            while len2: # Loop runs until the remainder is 0 i.e when we have found the GCD and its value is in len1
                len1, len2 = len2, len1 % len2 # We are continously dividing the number and its remainder until remainder is 0
            return len1 # and we are returning the GCD value
        return str1[:gcd(len(str1),len(str2))] # Using the slicing technique in py slice the string from index 0 until the GCD index
        
