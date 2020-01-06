class Solution:
    def maxSubArray(self, nums) -> int:
        """

        :param nums: input num list
        :return: max sub array list
        """

        max_sum = 0
        ans = 0

        for n in nums:

            if max_sum+n <= 0:
                max_sum = n
            else:
                max_sum = max([max_sum+n, n])

            ans = max([max_sum, ans])

        if len([each for each in nums if each < 0]) == len(nums):
            ans = max(nums)

        return ans


if __name__ == "__main__":
    input_list = [-1]
    sol = Solution()
    print(sol.maxSubArray(nums=input_list))
