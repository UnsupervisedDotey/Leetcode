class Solution:
    def maxProfit(self, prices) -> int:
        """
        :param prices: input prices list
        :return: max profit
        """

        low = float("Inf")
        profit = 0

        for p in prices:

            if p < low:
                low = p

            _profit = p - low

            if _profit > profit:
                profit = _profit

        return profit


if __name__ == "__main__":
    input_list = [7,1,4,3,4]
    sol = Solution()
    print(sol.maxProfit(prices=input_list))