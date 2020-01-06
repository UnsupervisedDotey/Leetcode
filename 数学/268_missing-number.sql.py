class Solution:
    def missingNumber(self, nums) -> int:

        nums.sort()
        tmp = 0

        for n in nums:
            # print(n, tmp)
            if tmp == n:
                tmp += 1
            else:
                return tmp

        return nums[-1]+1


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 0, 1]
    print(sol.missingNumber(nums=nums))
