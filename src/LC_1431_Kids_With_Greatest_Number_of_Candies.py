'''
Created on Oct 17, 2020
Given the array candies and the integer extraCandies, where candies[i] 
represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids 
such that he or she can have the greatest number of candies among them.
Notice that multiple kids can have the greatest number of candies.
@author: chrbl

Example 1:
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
Explanation: 
Kid 1 has 2 candies and if he or she receives all extra candies (3) will have 5 candies --- the greatest number of candies among the kids. 
Kid 2 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. 
Kid 3 has 5 candies and this is already the greatest number of candies among the kids. 
Kid 4 has 1 candy and even if he or she receives all extra candies will only have 4 candies. 
Kid 5 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. 
'''
from typing import List

candies = [2,3,5,1,3]
extraCandies = 3

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candyList = []
        maxCandy = max(candies)
        for candy in candies:
            if candy + extraCandies >= maxCandy:
                candyList.append(True)
            else:
                candyList.append(False)
        return candyList;
            
#From here down is purely testing the example given to see if we have a solution 
#The left side of the expression is our result, the right side is the correct result
#for the given example above attributed to 'myList'         
sol = Solution()
if (sol.kidsWithCandies(candies, extraCandies) == [True,True,True,False,True]):
    print(True)
else:
    print(False)

''' This solution was successful on LeetCode. Used lines 28-35 (the rest was for working/testing locally and not in browser)
    Lines: 8, Runtime: 40ms, Memory: 14.2MB, Time Complexity: O(n)
    Theory behind the solution: 
    I read the description and figured would find the max value in our candies array, then use that number to compare to when we
    loop back through adding 'extraCandies'. If the number is higher with extraCandies, then that index in our returned list
    must be true.
    This is O(n) as the solution is limited by both the max function (O(n)) and searching through the for loop to determine how many 
    total candies a kid may have. I do not believe we can get any better time complexity out of this as we must match index
    to index the candy list and the return list with logic applied to each element.
    
'''