class Solution:
    def searchInsert(self, nums, target) -> int:
        try:
            res = nums.index(target)
        except:
            nums.append(target)
            nums.sort()
            res = nums.index(target)

        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, 5, 6]
    target = 0
    print(sol.searchInsert(nums=nums, target=target))
