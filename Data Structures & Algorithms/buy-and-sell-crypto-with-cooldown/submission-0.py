class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold = 0
        buy = 0
        hold = -float('inf')
        
        
        for price in prices:
            prev_sold = sold 
            
            hold = max(hold ,buy - price )
            
            sold = hold + price
            
            buy = max(buy, prev_sold)
            
            
        
        return max(buy,sold)