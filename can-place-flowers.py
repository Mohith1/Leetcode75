'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
https://leetcode.com/problems/can-place-flowers
'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            # check if the current plot is empty
            if flowerbed[i] == 0:
                # check if the left and right plot are empty
                empty_left_plot = (i==0) or (flowerbed[i-1] == 0) 
                empty_right_plot = (i == len(flowerbed) - 1) or (flowerbed[i+1] == 0) '''Here although you might feel it might throw Index Out of Bounds error
  as we trying to access flowerbed[i+1] it would not as, If i is at the last index, the second part of the condition (flowerbed[i+1] == 0) won't be evaluated due to short-circuiting in Python. 
  Short-circuiting means the expression is evaluated from left to right, and if the first part is True, Python won't evaluate the second part at all.
  
&& (AND): If the first condition is false, the second condition is not evaluated.
|| (OR): If the first condition is true, the second condition is not evaluated.'''
                
# If both plots are empty, we can plant a flower here.
                if empty_left_plot and empty_right_plot:
                    flowerbed[i] = 1
                    count += 1
                    if count >=n:
                        return True
        return count >= n
