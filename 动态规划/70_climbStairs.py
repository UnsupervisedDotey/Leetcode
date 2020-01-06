# import pysnooper


class Solution:
    # @pysnooper.snoop()
    def climbStairs(self, n: int) -> int:

        if n <= 0:
            res = 0

        elif n == 1:
            res = 1

        else:
            _1 = 1
            _2 = 1
            res = 0
            for stair in range(2, n+1):
                res = _1 + _2
                _2 = _1
                _1 = res

        return res


if __name__ == "__main__":
    sol = Solution()
    input_n = 4
    print(sol.climbStairs(n=input_n))
