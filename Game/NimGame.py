'''
class Solution:
    def canWinNim(self, n):

         if n%4 == 0:
            return False
         else:
            return True

'''
class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0


sol = Solution()
print(sol.canWinNim(4))