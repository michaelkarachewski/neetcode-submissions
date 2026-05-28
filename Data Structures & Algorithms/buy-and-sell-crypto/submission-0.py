class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0

        output = 0
        maxval = prices[len(prices)-1]

        for curval in reversed(prices):
            output=max(output,maxval-curval)
            maxval=max(maxval,curval)


        
        return output
        