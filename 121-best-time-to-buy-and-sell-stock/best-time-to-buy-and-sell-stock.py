class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """


        best = 0

        buy_price = prices[0]

        for x in prices:

            if x<buy_price:
                buy_price = x

            profit = x - buy_price
            best = max(profit,best)

        return best







            





        