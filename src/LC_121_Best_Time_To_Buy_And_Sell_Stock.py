'''
Created on Jan 31, 2021
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
@author: chrbl
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''

from typing import List

prices = [7,1,5,3,6,4]

#Brute force O(n^2) 
#This was so inefficient Leetcode could not run it and my computer terminated the program,
#let's optimize for one pass O(n) time complexity
class SolutionOld:
    def maxProfitOld(self, prices: List[int]) -> int:
        maxP = 0
        for i in range(len(prices)-1):
            for j in range(i, len(prices)):
                if(prices[j]-prices[i] > maxP):
                    maxP = prices[j]-prices[i]         
        return maxP
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:   
        maxP = 0
        minPrice = prices[0]
        for price in prices:
            if price < minPrice:
                minPrice = price
            if price - minPrice > maxP:
                maxP = price - minPrice
        return maxP
    
    
    
#From here down is purely testing the example given to see if we have a solution 
#The left side of the expression is our result, the right side is the correct result
#for the given example above attributed to 'myList'         
sol = Solution()
if (sol.maxProfit(prices) == 5):
    print(True)
else:
    print(False)
        
''' This solution was successful on LeetCode. Used lines 35-42 (the rest was for working/testing locally and not in browser)
    Lines: 8, Runtime: 1116ms, Memory: 25.3MB, Time Complexity: O(n)
    Theory behind the solution: 
    The old solution above is very inefficient, it was my first brute force attempt at solving this, unfortunately was so
    inefficient that it is basically useless. It takes each number and looks at the rest of the list to determine the max profit
    if you were to buy stocks on that day. Then compares that to every other day down the list.
    The Second solution keeps track of a minimum price, this min price is used to determine if you invested on whatever day minprice
    fell on, what is the best return based on whats left in the list(which we access as we progress through the loop). At the end of 
    the loop we know the minimum price before the largest day of return.  
    This is O(n) as the solution takes O(n) time to look through each initial price and that is all. it does takes a little storage
    to remember the minimum price but compared to the first solution, that storage space is negligible compared to runtime.
'''   