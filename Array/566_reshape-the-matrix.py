class Solution:
    def matrixReshape(self, nums, r: int, c: int):
        """
        function description

        """
        _r = len(nums)
        _c = len(nums[0])
        
        if r*c > _r*_c:
            return nums

        else:
            pure = []
            for ns in nums:
                for n in ns:
                    pure.append(n)
            
            res = []
            for i in range(c, len(pure)+1, c):
                res.append(pure[i-c:i])
            return res


if __name__ == "__main__":
    sol = Solution()
    nums = [[1,2],[3,4],[5,6]]
    r = 6
    c = 1
    print(sol.matrixReshape(nums, r, c))
