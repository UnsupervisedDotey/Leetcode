class Solution:
    def fixedPoint(self, A) -> int:
        # print(A)
        for i in range(len(A)):
            if i == A[i]:
                # print(i, A[i])
                return i

        return -1


if __name__ == "__main__":
    sol = Solution()
    A = [-10,-5,3,4,7,9]
    print(sol.fixedPoint(A=A))
