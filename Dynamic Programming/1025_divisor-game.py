class Solution:
    def divisorGame(self, N: int) -> bool:

        dp = [False for i in range(N+1)]
        if N >= 1:
            dp[1] = False
        if N >= 2:
            dp[2] = True

        for _n in range(3, N+1):
            for _divisor in range(1, _n):

                # print(_n, _divisor, dp, dp[_divisor])
                if _n % _divisor == 0 and dp[_divisor]:
                    dp[_n] = True
                    break

        return dp[N]


if __name__ == "__main__":
    sol = Solution()
    for i in range(2):
        N = 1
        print(sol.divisorGame(N=i))
