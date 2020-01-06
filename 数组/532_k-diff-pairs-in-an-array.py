class Solution:
    def findPairs(self, nums, k: int):
        if k < 0:
            return 0
        saw = set()
        diff = set()
        for i in nums:
            if i - k in saw:
                diff.add(i - k)
            if i + k in saw:
                diff.add(i)
            saw.add(i)
        return len(diff)


if __name__ == "__main__":
    sol = Solution()
    nums = [3,1,4,1,5]
    k = 2
    print(sol.findPairs(nums=nums, k=k))
