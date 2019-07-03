class Solution:
    def minCostClimbingStairs(self, cost) -> int:

        res = 0
        _left = 0
        _right = 0
        _current = -1
        costs = cost
        cost = cost + [0, 0]

        while _current < len(costs):

            _left = _current + 1
            _right = _current + 2

            print(_left, _right, _current)

            costs_tmp = [cost[_left], cost[_right]]
            index_tmp = [_left, _right]

            if cost[_left] != cost[_right]:
                _min_index = costs_tmp.index(min(costs_tmp))
            else:
                _min_index = 1

            _current = index_tmp[_min_index]
            res += cost[_current]

        return res


if __name__ == "__main__":

    input_list = [5, 15, 20]    # [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    sol = Solution()
    print(sol.minCostClimbingStairs(cost=input_list))
