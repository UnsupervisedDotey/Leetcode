class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None:
            return None

        separate = s.split(" ")

        result = ""
        for each in separate:
            result += each[::-1]
            result += " "

        return(result[:-1])


sol = Solution()
print(sol.reverseWords("Let's take LeetCode contest"))