class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        我可能是个傻子
        题目中说了众数的个数大于n/2,排序完第nums[n/2]不就是众数么!
        return sorted(nums)[len(nums)/2]
        '''
        nums.sort()
        prev = nums[0]
        maj = 0
        map = dict()

        for each in nums:

            if prev == each:
                maj += 1
                prev = each
                map[prev] = maj
            else:

                maj = 1
                prev = each

        majority = max(map.items(), key=lambda x: x[1])

        if majority[1] > (len(nums)/2):
            return majority[0]
        else:
            return None


sol = Solution()
print(sol.majorityElement([2,2,1,1,1,2,2]))