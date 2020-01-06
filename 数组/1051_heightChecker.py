class Solution:
    def heightChecker(self, heights) -> int:

        sorted_heights = sorted(heights)

        index = [i for i in range(len(sorted_heights)) if sorted_heights[i] != heights[i]]

        return len(index)


if __name__ == '__main__':

    sol = Solution()
    input_list = [1, 1, 1, 1, 1, 1, 1, 1]

    print(
        sol.heightChecker(
            heights=input_list
        )
    )
