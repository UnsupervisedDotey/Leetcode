import operator


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        if len(matrix) == 1 or len(matrix[0]) == 1:
            return True

        res = 1
        for i in range(1, len(matrix)):
            # print(matrix[i][1:], matrix[i - 1][:-1])
            if operator.eq(matrix[i][1:], matrix[i - 1][:-1]):
                res *= 1
            else:
                res *= 0

        if len(matrix[0]) == 2 and len(matrix) == 2:
            res *= matrix[0][0] == matrix[-1][-1]

        return res == 1


if __name__ == "__main__":
    matrix = [[97, 97],
            [80, 97],
            [10, 80]
            ]

    sol = Solution()
    print(sol.isToeplitzMatrix(matrix=matrix))
