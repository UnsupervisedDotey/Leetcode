import random
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n - 1)

        length = factorial(len(nums))
        permutations = []
        for each in range(length):
            permutations.append([])

        for j in range(len(permutations)):

            current = [n for n in nums]
            each = [n for n in nums]
            allDiff = True
            # print(j, allDiff)

            if j > 0:
                for a in range(j+1):
                    if each == permutations[a]:
                        allDiff = allDiff and False
                hi = 0
                while allDiff is False:
                    current = [n for n in nums]
                    for i in range(len(each)):

                        num = random.sample(current, 1)[0]
                        #print(num)
                        each[i] = num
                        current.remove(num)

#                    print(j, allDiff, each, permutations)
                    allDiff = True
                    for a in range(j + 1):
                        if each == permutations[a]:
                            allDiff = allDiff and False

                    hi += 1
            else:
                for i in range(len(each)):
                    num = random.sample(current, 1)[0]

                    each[i] = num
                    current.remove(num)

            permutations[j] = each

        return permutations


sol = Solution()
print(sol.permute([1,2,3]))