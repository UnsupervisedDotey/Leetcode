class Solution:
    def getRow(self, rowIndex: int):
        """
        给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

        :param rowIndex:
        :return:
        """

        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1, 1]

        rowIndex += 1
        res = []

        for i in range(1, rowIndex + 1):
            res.append([1] * i)

        _saved = res[-1]
        to_be_used = res[-1]

        for row in range(2, rowIndex):

            for th in range(1, row):

                if th <= row / 2:
                    res[row][th] = _saved[th] + _saved[th - 1]
                elif th > row / 2:
                    res[row][th] = res[row][row - th]

                to_be_used[th] = res[row][th]

            _saved = to_be_used.copy()

        return res[-1]


if __name__ == "__main__":
    sol = Solution()
    rowIndex = 3
    print(sol.getRow(rowIndex=rowIndex))
