"""
给定两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

示例 1:

输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
    对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
    对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。

"""
from typing import List
from collections import defaultdict


class Solution:

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums2_dict = defaultdict(list)

        for index, n in enumerate(nums2):
            for each in reversed(nums2[index + 1::]):
                nums2_dict[n].append(each)

        # print(nums2_dict)
        for _ in nums1:

            while nums2_dict[_]:
                each = nums2_dict[_].pop()
                # print(_, each, nums2_dict, res)
                if each > _:
                    res.append(each)
                    break
            else:
                res.append(-1)

        return res


if __name__ == "__main__":
    sol = Solution()
    # nums1 = [4, 1, 2]
    # nums2 = [1, 3, 4, 2]
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    print(sol.nextGreaterElement(nums1=nums1, nums2=nums2))
