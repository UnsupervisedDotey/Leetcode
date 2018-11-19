class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        这他妈的是什么
        
        global out,s
        s = []
        out = [[]]
        def dfs(i):
            global out,s

            for j in range(i,len(nums)):

                s.append(nums[j])

                out.append(s[:])

                dfs(j+1)
                s = s[:len(s)-1]


        dfs(0)

        return out
        """

        subset = []
        subset.append([])

        for each in nums:
            for sets in subset:
                if sets is not None:
                    # print("before: ", [each], sets, subset)

                    if len(sets) == 1 and each == sets[0]:
                        break

                    if sets is not []:
                        new = []
                        for prev in sets:
                            new.append(prev)
                        new.append(each)
                        subset.append(new)

                    if sets is []:
                        subset.append([each])

                    subset = [str for str in subset if str is not None]
                    # subset.append([])

                    # print("after: ", [each], sets, subset)

        return subset

sol = Solution()
print(sol.subsets([1, 2, 3, 4, 5]))
