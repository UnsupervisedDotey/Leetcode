class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        """
        给定一个二进制数组， 计算其中最大连续1的个数。

        :param nums:
        :return:
        """
        all_max = 0
        tmp = 0

        for n in nums:
            if n:
                tmp += 1
            else:
                if tmp > all_max:
                    all_max = tmp
                tmp = 0

        return max([all_max, tmp])

if __name__ == "__main__":
    sol = Solution()
    nums = []
    print(sol.findMaxConsecutiveOnes(nums=nums))
