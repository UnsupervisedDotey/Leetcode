import pysnooper


class Solution:

    # @pysnooper.snoop()
    def titleToNumber(self, s: str) -> int:

        my_dict = dict(zip(
            [chr(x) for x in range(ord('A'), ord('Z') + 1)],
            [i for i in range(1, 27)]))

        number = 0
        digit = 0
        for i in range(len(s)-1, -1, -1):
            if digit == 0:
                number += my_dict[s[i]]

            elif digit >= 1:
                number += my_dict[s[i]] * 26 ** digit

            digit += 1

        return number


if __name__ == "__main__":

    sol = Solution()
    input_str = "AAA"
    print(sol.titleToNumber(s=input_str))
