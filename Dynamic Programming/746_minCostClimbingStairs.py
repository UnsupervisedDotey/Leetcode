class Solution:
    def minCostClimbingStairs(self, cost) -> int:

        if len(cost) == 2:
            return min(cost)

        res = 0

        costs = cost
        cost = cost + [0, 0, 0, 0]

        for i in range(len(costs)):

            power_1 = res + cost[i] + min(cost[i+1], cost[i+2])

            if i == 0:
                res = power_1

            if power_1 < res:
                res += cost[i]

        return res


if __name__ == "__main__":

    input_list = [1, 0, 2, 2]
    sol = Solution()
    print(sol.minCostClimbingStairs(cost=input_list))
