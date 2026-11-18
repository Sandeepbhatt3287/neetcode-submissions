class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices) -1
        profit =0
        for i in range(n):
            cur = 0
            for j in range(i+1,n):
                cur =  prices[j] - prices[i] 
                profit = max(profit, cur)
        
        return profit
