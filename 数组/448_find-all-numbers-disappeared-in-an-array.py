class Solution:
    def findDisappearedNumbers(self, nums):

        if nums == []:

            return []
        else:
            ans = list(set(range(1, len(nums)+1)) - set(nums))

            return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 5]
    print(sol.findDisappearedNumbers(nums=nums))
