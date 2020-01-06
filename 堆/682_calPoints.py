class Solution:
    def calPoints(self, ops) -> int:

        score = 0
        last_valid_score = []

        for each in ops:
            if each == "C":
                score, last_valid_score = self.c(score, last_valid_score=last_valid_score)

            elif each == "D":
                score, last_valid_score = self.d(score, last_valid_score=last_valid_score)

            elif each == "+":
                score, last_valid_score = self.plus(score, last_valid_score=last_valid_score)

            else:
                score += int(each)
                last_valid_score.append(int(each))
            # print("out", score, last_valid_score)

        return score

    def plus(self, score, last_valid_score):
        """2. "+"（一轮的得分）：表示本轮获得的得分是前两轮有效 回合得分的总和。"""

        tmp = last_valid_score[-1] + last_valid_score[-2]
        score = score + tmp

        return score, last_valid_score + [tmp]

    def c(self, score, last_valid_score):
        """4. "C"（一个操作，这不是一个回合的分数）：表示您获得的最后一个有效 回合的分数是无效的，应该被移除。"""

        score = score - last_valid_score[-1]
        del last_valid_score[-1]

        return score, last_valid_score

    def d(self, score, last_valid_score):
        """3. "D"（一轮的得分）：表示本轮获得的得分是前一轮有效 回合得分的两倍。"""

        tmp = 2*last_valid_score[-1]
        score = score + tmp

        return score, last_valid_score + [tmp]


if __name__ == "__main__":
    sol = Solution()
    input_list = ["5", "2", "C", "D", "+"]
    print(sol.calPoints(ops=input_list))
