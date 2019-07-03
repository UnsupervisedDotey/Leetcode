class Solution:
    def minCostClimbingStairs(self, cost) -> int:

        if len(cost) == 2:
            return min(cost)

        res = 0
        _current = -1

        costs = cost
        cost = cost + [0, 0, 0, 0]

        while _current < len(costs):

            power_1 = cost[_current+1] + min(cost[_current+2], cost[_current+3])
            power_2 = cost[_current+2] + min(cost[_current+3], cost[_current+4])

            print(power_1, power_2)

            if power_1 < power_2:
                _current = _current+1
            else:
                _current = _current+2

            res += cost[_current]

        return res


if __name__ == "__main__":

    input_list = [1, 0, 2, 2]
    sol = Solution()
    print(sol.minCostClimbingStairs(cost=input_list))
