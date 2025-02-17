'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

https://leetcode.com/problems/increasing-triplet-subsequence
'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        nums_i = nums_j = float('inf') 
        '''Intialize both variables to Infinity that is the maxium possible value. Intution is i < j and nums[i] < nums[j] if you find a number greater than nums[j] -> return True. 
        Else return False
        '''
        for i in range(len(nums)): 
            if nums[i] <= nums_i: #Store the intial value to nums_i and check if any value is less than the current value if yes replace.
                nums_i = nums[i]
            elif nums[i] <= nums_j: #Store the value to nums_j which is more than nums_i as we are check the value after 1st if condition and stores its values to nums_j
                nums_j = nums[i]
            else: #Now if control reaches this else block it means whatever value is the current value it is greater than nums_i and nums_j, so simply return true
                return True
        return False #If none of above is true. Return False
