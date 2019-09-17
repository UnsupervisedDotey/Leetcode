from collections import defaultdict
from itertools import combinations

def flat(deep_list):
    for element in deep_list:
        if isinstance(element, list):
            yield from flat(element)
        else:
            yield element


class Solution:
    def containsNearbyDuplicate(self, nums, k):

        d = defaultdict(list)

        for i in range(len(nums)):
            d[nums[i]].append(nums.index(nums[i], i))

        # print(d)

        ans = [[abs(each[1]-each[0]) for each in list(combinations(value, 2))] for value in d.values()]
        tocheck = [i for i in flat(ans)]

        if len(tocheck) < 1:
            return False
        else:
            return min(tocheck) <= k


if __name__ == "__main__":
    sol = Solution()
    nums = [1]
    k = 1
    print(sol.containsNearbyDuplicate(nums=nums, k=k))
