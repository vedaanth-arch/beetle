class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=float('inf')
        max_profit=0
        for i in prices:
            if i<min_price:
                min_price=i
            else:
                profit=i-min_price
                max_profit=max(profit,max_profit)
        return max_profit
        '''i have to determine the profit by selecting one day as buying day n one day as selling day and subtracting btw thm both '''