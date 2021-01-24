'''
Created on Jan 23, 2021
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
@author: chrbl

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

from typing import List

nums = [2,7,11,15]
target = 9

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for operator1 in range(0, len(nums)-1):
            for operator2 in range(operator1+1, len(nums)):
                if nums[operator1] + nums[operator2] == target:
                    return [operator1, operator2]
        
#From here down is purely testing the example given to see if we have a solution 
#The left side of the expression is our result, the right side is the correct result
#for the given example above attributed to 'myList'         
sol = Solution()
if (sol.twoSum(nums, target) == [0, 1]):
    print(True)
else:
    print(False)
    
    
''' This solution was successful on LeetCode. Used lines 24-27 (the rest was for working/testing locally and not in browser)
    Lines: 4, Runtime: 52ms, Memory: 14.5MB, Time Complexity: O(nLogn)
    Theory behind the solution: 
    I decided to add each number to each number to its 'right' in the array. This allows me to check every number against every other
    number and not having to repeat using the commutative property of addition. This is the brute force method for solving this
    problem and we can do better.
    This is O(n^2) as the solution takes O(n) time to look through each initial number and takes O(n) to look through each
    number remaining in the list. 
'''   
    