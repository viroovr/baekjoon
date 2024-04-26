import copy
from random import randint


class Solution():
    def __init__(self) -> None:
        # self.testCaseNum = 1
        self.testCaseNum = int(input())

    def main(self):
        # TEST_NUM = 3000
        for _ in range(self.testCaseNum):
            # self.conveStoreNum = 100
            # self.departure = (-TEST_NUM, -TEST_NUM)
            # self.conveStoreCoords = [
            #     (randint(-TEST_NUM, TEST_NUM), randint(-TEST_NUM, TEST_NUM)) for _ in range(self.conveStoreNum)]
            # self.destination = (TEST_NUM, TEST_NUM)
            self.conveStoreNum = int(input())
            self.departure = tuple(map(int, input().split()))
            self.conveStoreCoords = [
                tuple(map(int, input().split())) for _ in range(self.conveStoreNum)]
            self.destination = tuple(map(int, input().split()))
            ans = self.get_answer()
            print(ans)

    def get_answer(self):
        queue = []
        queue.append(self.departure)
        while queue:
            x, y = queue.pop(0)
            if self.is_in_range(x, y, self.destination):
                return "happy"
            temp = copy.copy(self.conveStoreCoords)
            deleteCoords = []
            for i, coord in enumerate(temp):
                if self.is_in_range(x, y, coord):
                    deleteCoords.append(i)
                    queue.append(coord)
            for i in reversed(deleteCoords):
                self.conveStoreCoords.pop(i)
        return "sad"

    def is_in_range(self, x, y, cord):
        return abs(x - cord[0]) + abs(y - cord[1]) <= 1000


sol = Solution()
sol.main()
