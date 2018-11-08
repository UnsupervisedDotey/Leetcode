class Solution(object):
    def singleNumber(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """

        increase = sorted(nums)

        first = 0
        n1 = float('inf')
        for each in increase:

            if first == 0:

                n1 = each
                first = 1
                if (each == increase[-1]):
                    return each
            else:
                if (n1 == each):
                    first = 0
                else:
                    return n1




sol = Solution()
print(sol.singleNumber([2,2,1,3,3]))