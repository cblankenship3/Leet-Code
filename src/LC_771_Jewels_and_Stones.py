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
        jMap = set(J)   #for this example this is equal to "jMap = {"a","A"}" just 
                        #faster than looping through each element and adding to jMap
        return sum([i in jMap for i in S])
            
#From here down is purely testing the example given to see if we have a solution 
#The left side of the expression is our result, the right side is the correct result
#for the given example above attributed to 'myList'         
sol = Solution()
if (sol.numJewelsInStones(j,s) == 3):
    print(True)
else:
    print(False)

''' This solution was successful on LeetCode. Used lines 20-22 (the rest was for working/testing locally and not in browser)
    Lines: 2, Runtime: 24ms, Memory: 14.2MB, Time Complexity: O(n)/O(m+n)
    Theory behind the solution: 
    Line 20 I made a set out of the jewel list. Any type of hash-based collection will work here.
    Line 22 we return the sum of where we find a jewel match. look for every instance of jMap[1], then jMap[2],... jMap[n] in S, 
    if a match is found, the function adds one to a running sum.
    This is O(n+m) as the solution is limited by and only by the amount of numbers in a given Jewel list and Stones List.
    Using a hash-based collection and the functions on it allow for a O(1) search on O(n) elements. We add O(m) for filling our 
    set with the Jewels list.
'''