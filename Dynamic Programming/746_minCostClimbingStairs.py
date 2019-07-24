class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        """
        最小花费爬楼梯
        [10, 15]        n=2        min(10, 15)=10
        [10, 15, 20]    n=3        min(20 + min(10,15), 15) = 15

        登上i楼梯： i >2
            fun(i) = min(fun(i-1), fun(i-2))
        走过n楼梯：
            cost[i] + fun(i)

        :param cost:
        :return:
        """
        l = len(cost)

        dp = [0 for _ in range(l+1)]

        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, l):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
            # print(dp)

        return min(dp[l-1], dp[l-2])


if __name__ == "__main__":

    input_list = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    sol = Solution()
    print(sol.minCostClimbingStairs(cost=input_list))
