class Solution:
    def plusOne(self, digits):

        # return list(str(int("".join(map(lambda x: str(x), digits)))+1))
        tmp = 0
        for i in range(len(digits)):
            tmp += digits[i]*10**(len(digits)-1-i)

        return list(str(tmp+1))


if __name__ == "__main__":
    sol = Solution()
    digits = [1, 2, 9, 9]
    print(sol.plusOne(digits=digits))
