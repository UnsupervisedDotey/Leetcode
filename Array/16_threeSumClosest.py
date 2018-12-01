'''
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = sum(nums[:3])

        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l < r:
                temp = nums[i] + nums[l] +nums[r]
                if abs(res - target) > abs(temp-target):
                    res = temp
                elif target < temp:
                    r -=1
                else :
                    l +=1
        return res
'''


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()#从小到大排序
        length = len(nums)
        closest = []

        for i, num in enumerate(nums[0:-2]):#enumerate()枚举函数，把原列表变成序列

            l,r = i + 1,length - 1
            if num + nums[r] + nums[r - 1] <target: # 最大
                closest.append(num + nums[r] + nums[r - 1])
            elif num + nums[l] + nums[l+1] >target:# 最小
                closest.append(num + nums[l] + nums[l+1])
            else:
                while l <r :# 左右混合
                    closest.append(num + nums[l] + nums[r])
                    if num + nums[l] + nums[r] <target: #  数小，右移
                        l += 1
                    elif num + nums[l] + nums[r] > target:# 数大，左移
                        r -= 1
                    else:#相等
                        return target
        # 根据与target的距离排序，从小到大

        closest.sort(key = lambda x: abs(x - target))#lambda为匿名函数，方便求key和target的距离
        return closest[0]


sol = Solution()
print(sol.threeSumClosest([-1, 2, 1, -4], target=1))