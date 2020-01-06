class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.

        class Solution:
    def merge(self, nums1, m, nums2, n):
        for i in range(n):
            nums1[m] = nums2[i]
            m += 1
        nums1.sort()
        
        """

        p1 = m
        p2 = n
        for i in range(m + n - len(nums1)):
            nums1[i + m + n] = 0
        print(nums1)
        while p1 > 0 or p2 > 0:
            print(nums1)
            if p1 == 0:
                nums1[p2+p1-1] = nums2[p2-1]
                p2 -= 1
            elif p2 == 0:
                nums1[p2+p1-1] = nums1[p1-1]
                p1 -= 1
            elif nums1[p1-1] > nums2[p2-1]:
                nums1[p2+p1-1] = nums1[p1-1]
                p1 -= 1
            elif nums1[p1-1] <= nums2[p2-1]:
                nums1[p2+p1-1] = nums2[p2-1]
                p2 -= 1



sol = Solution()
nums1 = [-1,0,0,3,3,3,0,0,0]
nums2 = [1,2,2]
n = 3
m = 6
'''
[-1,0,0,3,3,3,0,0,0]
6
[1,2,2]
3
输出
[-1,1,2,2,3,3,3]
预期结果
[-1,0,0,1,2,2,3,3,3]
'''
print(sol.merge(nums1, m, nums2, n))
#print(sol.findIndexMax(nums1))