class Solution:
    def removeOuterParentheses(self, S: str) -> str:

        stack = []

        in_ = []
        out_ = 0

        primitive = ""

        for i in range(len(S)):
            if S[i] is "(":
                stack.append("(")
                if len(in_) == 0:
                    in_.append(i)
            else:
                stack.pop(0)
                out_ = i

            if i > 0 and len(stack) == 0:
                # print(primitive)
                primitive = primitive + S[in_[0]+1: out_]
                in_ = []

        return primitive


if __name__ == "__main__":
    sol = Solution()
    input_str = "(()())(())(()(()))"

    print(
        sol.removeOuterParentheses(
            S=input_str
        )
    )
