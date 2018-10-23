class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) > 0:
            low = prices[0]
            benefit = 0

            for each in prices:
                if each <= low:
                    low = each
                else:
                    temp = each - low
                    if temp > benefit:
                        benefit = temp

            return benefit
        else:
            return 0


sol = Solution()
print(sol.maxProfit([7,6,4,3,1]))
