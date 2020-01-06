'''
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        length = len(s) - 1

        final = ""
        for i in range(length, -1, -1):
            final += s[i]

        return final

'''

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

sol = Solution()
print(sol.reverseString("A man, a plan, a canal: Panama"))