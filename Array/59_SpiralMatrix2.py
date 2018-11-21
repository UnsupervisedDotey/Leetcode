class Solution(object):
    def generateMatrix(self, n):

        nums = [each for each in range(1, n**2 + 1)]
        matrix = []

        for each in range(n):
            matrix.append(nums[:n])

        left = 0
        right = n - 1
        minn = 1
        maxx = n - 1
        upDown = [1, -1, -1, 1] * n

        i = 0
        twice = 0
        for num in nums[n:]:

            if twice == 0 and upDown[i] == 1:                               # 左 +
                if left != maxx:
                    left += 1

                    matrix[left][right] = num
                    if left == maxx:
                        maxx -= 1
                        twice = 1
                        i += 1

            elif twice == 0 and upDown[i] == -1:                           # 左 -
                if left >= minn:
                    left -= 1

                    matrix[left][right] = num
                    if left < minn:

                        twice = 1
                        i += 1

            elif twice == 1 and upDown[i] == -1:                               # 右 -
                if right >= minn:
                    right -= 1

                    matrix[left][right] = num
                    if right < minn:
                        twice = 0
                        i += 1
                        minn += 1

            elif twice == 1 and upDown[i] == 1:                               # 右 +
                if right != maxx:
                    right += 1

                    matrix[left][right] = num
                    if right == maxx:

                        twice = 0
                        i += 1

        return matrix


sol = Solution()
print(sol.generateMatrix(5))