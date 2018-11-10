class Solution(object):
    def maxProfit(self, prices):

        """
        贪心算法
        :type prices: List[int]
        :rtype: int
        """
        if prices is None:
            return None

        profit = 0
        for i in range(0, len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        return profit

sol = Solution()
print(sol.maxProfit([1,2,3,4,5]))