class Solution:
    def rob(self, nums) -> int:
        new_nums = [0, 0] + nums
        l = len(new_nums)
        dp = [0] * l

        for i in range(2, l):
            dp[i] = max([dp[i-2] + new_nums[i], dp[i-1]])
            # print(dp, dp[i-2], new_nums[i], dp[i-1])

        return dp[-1]


if __name__ == "__main__":
    nums = [0]     # [2, 7, 9, 3, 1]
    Sol = Solution()
    print(Sol.rob(nums=nums))
