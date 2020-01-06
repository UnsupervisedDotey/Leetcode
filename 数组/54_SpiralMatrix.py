class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]: return []
        m, n = len(matrix), len(matrix[0])
        visited = [[0] * n for _ in range(m)]
        res = []
        self.row, self.col = 0, 0
        def spiral():
            move = False
            while self.col < n and not visited[self.row][self.col]:
                res.append(matrix[self.row][self.col])
                visited[self.row][self.col] = 1
                self.col += 1
                move = True
            self.col -= 1
            self.row += 1
            while self.row < m and not visited[self.row][self.col]:
                res.append(matrix[self.row][self.col])
                visited[self.row][self.col] = 1
                self.row += 1
                move = True
            self.row -= 1
            self.col -= 1
            while self.col >= 0  and not visited[self.row][self.col]:
                res.append(matrix[self.row][self.col])
                visited[self.row][self.col] = 1
                self.col -= 1
                move = True
            self.col += 1
            self.row -= 1
            while self.row >= 0 and not visited[self.row][self.col]:
                res.append(matrix[self.row][self.col])
                visited[self.row][self.col] = 1
                self.row -= 1
                move = True
            self.row += 1
            self.col += 1
            if move:
                spiral()
        spiral()
        return res


sol = Solution()
print(sol.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))