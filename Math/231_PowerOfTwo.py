class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        '''
        我是
        傻子
        if n <= 0:
            return False
        k = int(math.log(n, 2))       
        return 2 ** k == n
        
        '''

        for i in range(100):

            if 2**i == n:
                return True

        return False


sol = Solution()
print(sol.isPowerOfTwo(218))