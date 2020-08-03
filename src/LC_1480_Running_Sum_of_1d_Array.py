'''
Created on Aug 2, 2020
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]...nums[i]).

Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
@author: Chris Blankenship
'''
from typing import List

myList = [1,2,3,4] #this is the first example given, let's see how it works

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [nums[0]]
        for count in range(len(nums)-1):
            result.append(nums[count+1] + result[-1])
        return result
            
#From here down is purely testing the example given to see if we have a solution 
#The left side of the expression is our result, the right side is the correct result
#for the given example above attributed to 'myList'         
sol = Solution()
if (sol.runningSum(myList) == [1,3,6,10]):
    print(True)
else:
    print(False)

''' This solution was successful on LeetCode. Used lines 19-22 (the rest was for working/testing locally and not in browser)
    Lines: 4, Runtime: 40ms, Memory: 14.2MB, Time Complexity: O(n)
    Theory behind the solution: 
    I made a new list on line 19, we could have changed 'nums' to save space, however I wanted to keep inputs and 
    outputs differentiated.
    After assigning the value at the first index of nums I'm able to use result[-1] in infinitum, though this results
    in the iteration of nums with an offset of 1
    This is O(n) as the solution is limited by and only by the amount of numbers in a given list.
    This could be done with a while loop which may make for a slightly simpler solution, I ran this in Leetcode and got the 
    same runtime and space stats as the for loop shown here.
'''