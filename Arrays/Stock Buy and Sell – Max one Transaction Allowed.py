# GFG 160-Day DSA Challenge Progress

#-Day 6: Stock Buy and Sell – Max one Transaction Allowed
#   - Problem link: [https://www.geeksforgeeks.org/problems/stock-buy-and-sell-1587115620/](https://www.geeksforgeeks.org/problems/stock-buy-and-sell-1587115620/)
#  - Notes: This problem was a good reminder of a simple greedy approach. The key is to track the minimum price seen so far.

'''The Problem
The "Stock Buy and Sell - Max one Transaction Allowed" problem asks you to find the maximum profit you can achieve by buying and selling a stock exactly once. You are given an array of stock prices, where the i-th element is the price of the stock on day i. You must buy the stock on one day and sell it on a subsequent day.

Solution Approach
The most efficient approach to solve this problem is to iterate through the prices just once, keeping track of the minimum price seen so far and the maximum profit that can be made. This is a greedy approach.'''

#Solution
class Solution:
    def maximumProfit(self, prices):
        maxprofit=0
        profit=0
        buy=prices[0]
        for i in range(1,len(prices)):
            if prices[i]>=buy:
                profit=prices[i]-buy
                maxprofit=max(maxprofit,profit)
            else:
                buy=prices[i]
        
        return maxprofit
