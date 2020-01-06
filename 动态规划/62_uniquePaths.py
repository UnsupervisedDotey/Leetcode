'''
class Solution:
    def uniquePaths(self, m, n):

        if m == 1 or n == 1:
            return 1

        dynamicP =[[1 for _ in range(m)] for _ in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                dynamicP[i][j] = dynamicP[i-1][j] + dynamicP[i][j-1]

        return dynamicP[-1][-1]
'''


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        totalStep = m + n - 2
        minStep = min(m-1, n-1)
        fenzi = 1
        fenmu = 1
        for i in range(minStep, 0, -1):

            fenzi *= totalStep
            totalStep -= 1
            fenmu *= i
            a = fenzi
            b = fenmu
            while b != 0:
                r = b
                b = a % b
                a = r
            fenzi = int(fenzi / a)
            fenmu = int(fenmu / a)
        return int(fenzi / fenmu)


sol = Solution()
print(sol.uniquePaths(7, 3))