class Solution:
    def removeDuplicates(self, S: str) -> str:
        chars = set(S)
        sign = 1
        res = S
        # print(S, chars)
        while True:
            # print(res, sign)
            for c in chars:
                res = res.replace(c + c, "")
                sign = 1

            for c in chars:
                if c + c not in res:
                    sign = sign * 1
                else:
                    sign = sign * 0

            if sign == 1:
                break

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates(S="asdbbdsaf"))
