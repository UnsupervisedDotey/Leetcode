class Solution(object):
    def __init__(self):
        self.maxlen = 1
        self.index =  0

    def extendPalindrome(self, start, end, s, lens):
        while start >=0 and end < lens and s[start] == s[end]:
            start -=1
            end += 1
        if self.maxlen < end - start - 1:
            self.maxlen = end - start - 1
            self.index = start +1

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        lens = len(s)
        if lens < 2 :
            return s
        for i in range(lens-1):
            # if i*2 +1 > self.maxlen and (lens - i - 1)*2 + 1 > self.maxlen:
                self.extendPalindrome(i, i, s, lens)
            # if i*2 +2> self.maxlen and (lens - i - 1)*2 + 2 > self.maxlen:
                self.extendPalindrome(i, i+1, s, lens)
        return s[self.index : self.index + self.maxlen]


sol = Solution()
print(sol.longestPalindrome("babad"))
import pandas as pd
