class NumArray:

    def __init__(self, nums):
        # 这里可以改成dp求sum 不用函数
        self.sums = [0] + [sum(nums[0:l]) for l in range(1, len(nums)+1)]
        # print(self.sums)

    def sumRange(self, i: int, j: int) -> int:
        # print(self.sums[j+1], self.sums[i])
        return self.sums[j+1]-self.sums[i]


if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    i, j = 2, 5
    obj = NumArray(nums)
    param_1 = obj.sumRange(i, j)
    print(param_1)
