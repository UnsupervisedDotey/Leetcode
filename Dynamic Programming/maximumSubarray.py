class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_index = 0
        right_index = len(nums)-1
        maxSum = self.subMax(nums, left_index, right_index)

        return maxSum

    def subMax(self, nums, left_index, right_index):
        if left_index == right_index:
            return nums[left_index]

        center_index = (left_index + right_index)//2

        leftMax = self.subMax(nums, left_index, center_index)
        rightMax = self.subMax(nums, center_index+1, right_index)

        leftBorderMax = nums[center_index]
        leftBorderSum = nums[center_index]

        for i in range(center_index-1, left_index-1, -1):
            leftBorderSum += nums[i]
            if leftBorderSum > leftBorderMax:
                leftBorderMax = leftBorderSum

        rightBorderMax = nums[center_index+1]
        rightBorderSum = nums[center_index+1]

        for j in range(center_index+2, right_index+1):
            rightBorderSum += nums[j]
            if rightBorderSum > rightBorderMax:
                rightBorderMax = rightBorderSum

        borderSum = leftBorderMax + rightBorderMax

        return max(leftMax, rightMax, borderSum)


sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))