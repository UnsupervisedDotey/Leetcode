class Solution:
    def thirdMax(self, nums):
        """
        给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

        :param nums:
        :return:
        """
        nums = list(set(nums))
        nums.sort(reverse=True)

        if len(nums) >= 3:
            return nums[2]
        else:
            return max(nums)


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 1]
    print(sol.thirdMax(nums))
