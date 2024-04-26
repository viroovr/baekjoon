class Solution():
    K = 0
    moneyList = []

    def __init__(self) -> None:
        self.K = int(input())
        self.moneyList = [int(input()) for _ in range(self.K)]

    def main(self):
        totalMoney = self.get_answer()
        print(totalMoney)

    def get_answer(self):
        sumMoneyList = []
        for i in range(self.K):
            currentMoney = self.moneyList[i]
            if currentMoney == 0:
                sumMoneyList.pop()
            else:
                sumMoneyList.append(currentMoney)
        return sum(sumMoneyList)


sol = Solution()
sol.main()
