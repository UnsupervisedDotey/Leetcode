class Solution:
    def generate(self, numRows):

        res = []
        if numRows == 0:
            return res

        for i in range(1, numRows+1):
            res.append([1]*i)

        _saved = res[-1]
        to_be_used = res[-1]
        # 思路：明天写两行_saved 上下两行
        if numRows <= 2:
            return res

        else:
            for row in range(2, numRows):

                for th in range(1, row):
                    #print(row, th, _saved)
                    if th <= row/2:
                        res[row][th] = _saved[th] + _saved[th-1]
                    elif th > row/2:
                        res[row][th] = res[row][row-th]

                    to_be_used[th] = res[row][th]

                _saved = to_be_used.copy()

        return res


sol = Solution()
input = 9

print(sol.generate(input))