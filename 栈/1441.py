from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        for i in range(min(n, target[-1])):
            if i + 1 not in target:
                res = res + ["Push", "Pop"]
            else:
                res.append("Push")
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.buildArray(target=[2, 3, 4], n=4))
