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

        ===========================================
        初始状态：dp[0] = cost[0], dp[1] = cost[1]
        状态转移方程： dp[i] = min(dp[i-1],dp[i-2]) + cost[i]
        实际上是求到最后一个楼梯的下一个楼梯需要多少体力。

        所以dp的通用解法是: 1. 计算初始状态；
                         2. 计算dp列表的状态转移方程；
                         3.返回dp列表的最后一组方程解
        ===========================================

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
