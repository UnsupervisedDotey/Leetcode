class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        left_s = []
        right_t = []
        for _ in S:
            # print(_)
            if _ == "#" and len(left_s) != 0:
                left_s.pop()
            elif _ == "#" and len(left_s) == 0:
                pass
            else:
                left_s.append(_)

        for _ in T:
            # print(_)
            if _ == "#" and len(right_t) != 0:
                right_t.pop()
            elif _ == "#" and  len(right_t) == 0:
                pass
            else:
                right_t.append(_)

        # print(left_s, right_t)
        return "".join(left_s) == "".join(right_t)


if __name__ == "__main__":
    sol = Solution()
    print(sol.backspaceCompare(S = "ab#c", T = "ad#c"))
