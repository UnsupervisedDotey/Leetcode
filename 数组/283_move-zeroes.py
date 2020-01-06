class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = list(filter(lambda x: x!=0, nums))+list(filter(lambda x: x==0, nums))


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    sol = Solution()
    print(sol.moveZeroes(nums=nums))
