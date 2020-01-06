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

        '''
        nums.sort()
        for i in range(0,len(nums)-1,2):
            if nums[i]!=nums[i+1]:
                return nums[i]
                break
        return nums[-1]
        '''

        '''
        iX = 0
        for iTmp in nums:
            iX ^= iTmp      # 按位异或然后赋值     [2,2,1,3,3]
        return iX           # 太神奇了         iX = 2,0,1,2,1
        '''




sol = Solution()
print(sol.singleNumber([2,2,1,3,3]))