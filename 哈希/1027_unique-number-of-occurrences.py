from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        counts = Counter(arr).values()

        return len(counts) == len(set(counts))


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 2, 1, 1, 3]
    print(sol.uniqueOccurrences(arr=arr))
