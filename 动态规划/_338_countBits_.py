class Solution:
    def bits(self, n):
        res = []
        return res

    def countBits(self, num: int):
        """
        不愧是中等难度的动态规划，我连写出2进制数组都不会。

        :param num:
        :return:
        """

        nums = [n for n in range(num+1)]
        print(nums)
        return [1]


if __name__ == "__main__":
    sol = Solution()
    num_ = 2

    print(sol.countBits(num=num_))
