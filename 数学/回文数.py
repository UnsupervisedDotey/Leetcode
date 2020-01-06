# Determine whether an integer is a palindrome. Do this without extra space.
#
# click to show spoilers.
#
# Some hints:
# Could negative integers be palindromes? (ie, -1)
#
# If you are thinking of converting the integer to string, note the restriction of using extra space.
#
# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?
#
# There is a more generic way of solving this problem.
#
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if 0 <= x <= 9:
            return True
        elif x > 9:
            str1 = str(x)

            if len(str1) % 2 == 0 :
                half = int(len(str1)/2)
                prev_half = list(str1[:half])
                befo_half = list(str1[half:])[::-1]
                i = 0
                while (i < len(befo_half)):
                    if prev_half[i] == befo_half[i]:
                        i += 1
                    else:
                        return False
                return True
            else:
                half = int((len(str1)-1)/2)
                prev_half = list(str1[:half])
                print(prev_half)
                befo_half = list(str1[half+1:])[::-1]
                print(befo_half)
                i = 0
                while(i < len(befo_half)):
                    if prev_half[i] == befo_half[i]:
                        i += 1
                    else:
                        return False
                return True
        else:
            return False

tool = Solution()
print(tool.isPalindrome(22))