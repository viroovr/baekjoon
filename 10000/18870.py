class Solution():
    N = 0
    xCoords = None

    def __init__(self) -> None:
        self.N = int(input())
        self.xCoords = list(map(int, input().split()))

    def main(self):
        ans = self.get_answer_list()
        self.print_answer(ans)

    def print_answer(self, ans):
        print(" ".join(map(str, ans)))

    def get_answer_list(self):
        sortingXcoordsWithIndex = sorted(
            [(x, i) for i, x in enumerate(self.xCoords)], key=lambda x: x[0])
        # print(sortingXcoordsWithIndex)
        listLength = len(sortingXcoordsWithIndex)
        answerList = [0 for _ in range(listLength)]
        storedNumber, storedCount = sortingXcoordsWithIndex[0][0], 0
        for i in range(listLength):
            comparingNumber = sortingXcoordsWithIndex[i][0]
            if comparingNumber != storedNumber:
                storedNumber = comparingNumber
                storedCount += 1
            answerList[sortingXcoordsWithIndex[i][1]] = storedCount
        return answerList


sol = Solution()
sol.main()
