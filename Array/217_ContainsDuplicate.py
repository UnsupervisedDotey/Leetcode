class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if nums is None:
            return None

        dup = set(nums)
        if len(dup) < len(nums):
            return True
        else:
            return False

sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))