class Solution:
    def climbStairs(self, n):

        if n <= 0:
            return 0

        elif n == 1:
            return 1

        elif n == 2:
            return 2

        else:
            a = 1
            b = 2
            temp = 0

            for i in range(2, n):
                temp = a + b
                a = b
                b = temp
            return temp


sol = Solution()
print(sol.climbStairs(3))

"""
dontforget = dict()
else:
    if n in dontforget.keys():
        return dontforget[n]
    else:
        times = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        dontforget[n] = times
        return times
"""