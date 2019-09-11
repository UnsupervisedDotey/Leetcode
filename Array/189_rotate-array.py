class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)
        _ = [nums[i-k] if i-k <= len(nums)-1 else nums[0+i-len(nums)-k] for i in range(len(nums))]

        for i in range(len(nums)):
            nums[i] = _[i]

        # print([i-k if i-k <= len(nums)-1 else 0+i-len(nums)-k for i in range(len(nums))])
        # print(k)
        # print(_)
        # print(nums)


if __name__ == "__main__":
    sol = Solution()
    nums = [-1,-100,3,99]
    k = 2
    print(sol.rotate(nums=nums, k=k))
