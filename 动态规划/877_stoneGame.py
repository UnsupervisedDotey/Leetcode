class Solution:
    def stoneGame(self, piles) -> bool:
        """
        dp怎么还和DAG有向无环图搭上关系了

        :param piles:
        :return:
        """
        l = len(piles)
        alex = []
        lee = []
        for i in range(int(l/2)):

            pair = sorted([piles[0], piles[-1]], reverse=True)[0]
            alex.append(pair)    # 大的
            del piles[piles.index(pair)]
            print(piles)

            pair = sorted([piles[0], piles[-1]], reverse=True)[0]
            lee.append(pair)    # 小的
            del piles[piles.index(pair)]
            print(piles)

        print(alex, lee)

        if sum(alex) > sum(lee):
            res = True
        else:
            res = False

        return res


if __name__ == "__main__":
    sol = Solution()
    list_ = [3,7,2,3]
    print(sol.stoneGame(piles=list_))
