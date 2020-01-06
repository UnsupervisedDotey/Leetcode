class Solution:
    def reverse(self, num):
        if num == 1:
            return 0
        elif num == 0:
            return 1

    def flipAndInvertImage(self, A):

        _done = [[self.reverse(each) for each in list[::-1]] for list in A]

        return _done

sol = Solution()
input = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

print(sol.flipAndInvertImage(input))