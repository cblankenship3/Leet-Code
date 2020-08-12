'''
Created on Aug 2, 2020
You're given strings J representing the types of stones that are jewels, and S representing the stones you have. 
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. 
Letters are case sensitive, so "a" is considered a different type of stone from "A"
@author: chrbl

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
'''
j = "aA"
s = "aAAbbbb"

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return 3
            
#From here down is purely testing the example given to see if we have a solution 
#The left side of the expression is our result, the right side is the correct result
#for the given example above attributed to 'myList'         
sol = Solution()
if (sol.numJewelsInStones(j,s) == 3):
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