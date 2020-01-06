class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dup = sorted(list(set(nums)))

        for i in range(len(dup)):
            nums[i] = dup[i]

        return len(dup)

sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
