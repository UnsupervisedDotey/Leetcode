class NumArray:

    def __init__(self, nums):
        """
        本体重点sumRange会重复加载

        假设 sumrange 被调用 1000次，其参数完全相同。我们怎么能加快速度？
        我们可以用额外的空间换取速度。

        假设我们预先计算了从数字 0 到 k 的累积和。我们可以用这个信息得出 sum(i，j)

        动态转移方程： dp[i] = dp[i-1] + nums[i-1]; res = dp[j+1] - dp[i];
        初始条件 dp[0] = 0

        :param nums:
        """

        # 这里可以改成dp求sum 不用函数
        self.sums = [0] + [sum(nums[0:l]) for l in range(1, len(nums)+1)]

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j+1]-self.sums[i]


if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    i, j = 2, 5
    obj = NumArray(nums)
    param_1 = obj.sumRange(i, j)
    print(param_1)
