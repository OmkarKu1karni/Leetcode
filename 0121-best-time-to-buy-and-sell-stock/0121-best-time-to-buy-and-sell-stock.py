class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = float('-inf')
        profit = 0
        n = len(prices)
        for i in range(n-1) : 
            diff = prices[i+1] - prices[i]
            profit += diff
            if profit > maxi : 
                maxi = profit 
            if profit < 0 :
                profit = 0 
        if maxi < 0 :
            return 0 
        else : 
            return maxi
        