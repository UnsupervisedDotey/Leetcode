from collections import Counter
class Solution:
    def commonChars(self, A):
        counts = 0

        for i in range(len(A)):
            A[i] = Counter(A[i])

            if i == 0:
                prevk = set(A[i].keys())

                prevDict = dict()
                for k, v in A[i].items():
                    prevDict[k] = [v, float('Inf')]

            key = set(A[i].keys())

            _unionDict = dict()
            _unionKeys = prevk & key
            prevk = _unionKeys

            for k in _unionKeys:

                if A[i][k] >= min(prevDict[k]):

                    _unionDict[k] = min(prevDict[k])

                prevDict[k].append(A[i][k])

        res = []
        for key, value in _unionDict.items():
            current = [key]*value
            res += current

        return res


sol = Solution()
input = ["cool","lock","cook"]

print(sol.commonChars(input))