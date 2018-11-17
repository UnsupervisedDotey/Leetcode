class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        shortest = strs[0]
        for each in strs:

            if len(each) < len(shortest):
                shortest = each

        firstWord = list(shortest)

        result = ""
        i = 0
        sign_list = [1]*len(strs)

        for each_str in firstWord:
            j = 0
            for each_word in strs:
                # print(i, each_str, each_word[i], sign_list)
                if each_str == each_word[i]:
                    sign_list[j] = 0
                    j += 1
                else:
                    sign_list[j] = 1
                    j += 1

            if sum(sign_list) == 0:
                result += each_str
                i += 1
                sign_list = [1]*len(strs)
            else:
                return result
        return result


sol = Solution()
print(sol.longestCommonPrefix( ["dog","racecar","car"]))