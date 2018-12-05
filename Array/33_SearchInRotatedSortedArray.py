class Solution(object):
    def search(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if target not in nums:
            return -1
        else:
            return nums.index(target)


sol = Solution()
print(sol.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))