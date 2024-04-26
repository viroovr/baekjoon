import unittest


class Mash():
    width = 0
    height = 0
    box = None
    check = None

    def __init__(self) -> None:
        self.width, self.height = map(int, input().split())
        self.box = [list(map(int, input().split()))
                    for _ in range(self.height)]
        self.check = [[False for _ in range(self.width)]
                      for _ in range(self.height)]

    def get_box(self):
        return self.box

    def find_certain_tomato(self, t: int):
        pos_tomato = []
        for y in range(self.height):
            for x in range(self.width):
                if self.box[y][x] == t:
                    pos_tomato.append((x, y))
        return pos_tomato

    def get_side_of_ripen_tomato(self, ripen_tomato_list):
        directionNWSE = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        return_list = []
        for ripe_pos in ripen_tomato_list:
            x, y = ripe_pos
            for dx, dy in directionNWSE:
                X, Y = x + dx, y + dy
                if (self.is_in_box(X, Y) and self.is_unripen(X, Y) and not self.check[Y][X]):
                    self.check[Y][X] = True
                    return_list.append((X, Y))
        return return_list

    def is_in_box(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def is_unripen(self, x, y):
        return self.box[y][x] == 0

    def ripe_tomato(self, unripen_list):
        for x, y in unripen_list:
            self.box[y][x] = 1

    def set_ripen_tomato_fully_ripen(self, ripen):
        for x, y in ripen:
            self.box[y][x] = 2

    def is_end(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.box[y][x] == -1:
                    continue
                if self.box[y][x] != 2:
                    return False
        else:
            return True


class Tomato():
    ripen_tomato = []
    unripen_list = []

    def set_ripen_tomato(self, ripen):
        self.ripen_tomato = ripen

    def set_unripen_list(self, unripen):
        self.unripen_list = unripen

    def get_ripen_tomato(self):
        return self.ripen_tomato

    def get_unripen_list(self):
        return self.unripen_list


class Solution():
    mash = None
    tomato = None
    day_elapsed = 0

    def __init__(self) -> None:
        self.mash = Mash()
        self.tomato = Tomato()
        self.is_end_bool = False

    def increment_day(self):
        self.day_elapsed += 1

    def ripen_tomato(self):
        self.setting_tomato()
        if self.tomato.get_unripen_list():
            self.mash.ripe_tomato(self.tomato.get_unripen_list())
            self.increment_day()
        else:
            self.is_end_bool = True
        self.mash.set_ripen_tomato_fully_ripen(
            self.tomato.get_ripen_tomato())

    def setting_tomato(self):
        if len(self.tomato.get_ripen_tomato()) == 0:
            self.tomato.set_ripen_tomato(self.mash.find_certain_tomato(1))
        else:
            self.tomato.set_ripen_tomato(self.tomato.get_unripen_list())
        self.tomato.set_unripen_list(self.mash.get_side_of_ripen_tomato(
            self.tomato.get_ripen_tomato()))

    def is_end(self):
        if self.is_end_bool:
            if not self.mash.is_end():
                self.day_elapsed = -1
            return True
        return False


sol = Solution()
while not sol.is_end():
    sol.ripen_tomato()
else:
    print(sol.day_elapsed)


class solTest(unittest.TestCase):

    # def test_mash(self):
    #     self.assertEqual(sol.mash.height, 4)

    # def test_box(self):
    #     self.assertIsInstance(sol.mash.box, list)
    #     self.assertIsInstance(sol.mash.box[0], list)

    # def test_tomato(self):
    #     self.assertEqual(sol.mash.find_certain_tomato(1), [(5, 3)])
    #     self.assertEqual(len(sol.mash.find_certain_tomato(0)), 23)

    # def test_oneday_after(self):
    #     self.assertEqual(sol.day_elapsed, 1)
    #     self.assertEqual(sol.tomato.unripen_list,
    #                      [(5, 2), (4, 3)])
    #     self.assertEqual(sol.mash.find_certain_tomato(1),
    #                      [(5, 2), (4, 3)])

    # def test_first_case_days_after(self):
    #     while not self.sol.is_end():
    #         self.sol.ripen_tomato()
    # #     sol.ripen_tomato()
    #     self.assertEqual(self.sol.day_elapsed, 8)
    #     self.assertEqual(self.sol.tomato.get_unripen_list(),
    #                      [])
    #     self.assertEqual(self.sol.mash.find_certain_tomato(1),
    #                      [])
    #     self.assertEqual(self.sol.mash.find_certain_tomato(0),
    #                      [])

    # def test_second_case_days_after(self):
    #     while not self.sol.is_end():
    #         self.sol.ripen_tomato()
    #     self.assertEqual(self.sol.day_elapsed, -1)
    #     self.assertEqual(self.sol.tomato.get_unripen_list(),
    #                      [])
    #     self.assertEqual(self.sol.mash.find_certain_tomato(1),
    #                      [])
    #     self.assertEqual(self.sol.mash.find_certain_tomato(0),
    #                      [(0, 0)])

    def test_third_case_days_after(self):
        self.assertEqual(sol.day_elapsed, 6)
        self.assertEqual(sol.tomato.get_unripen_list(),
                         [])
        self.assertEqual(sol.mash.find_certain_tomato(1),
                         [])
        self.assertEqual(sol.mash.find_certain_tomato(0),
                         [])

    # def test_4_case_days_after(self):
    #     self.assertEqual(sol.day_elapsed, 14)
    #     self.assertEqual(sol.tomato.get_unripen_list(),
    #                      [])
    #     self.assertEqual(sol.mash.find_certain_tomato(1),
    #                      [])
    #     self.assertEqual(sol.mash.find_certain_tomato(0),
    #                      [])

    # def test_5_case_days_after(self):
    #     self.assertEqual(sol.day_elapsed, 0)
    #     self.assertEqual(sol.tomato.get_unripen_list(),
    #                      [])
    #     self.assertEqual(sol.mash.find_certain_tomato(1),
    #                      [])
    #     self.assertEqual(sol.mash.find_certain_tomato(0),
    #                      [])


if __name__ == "__main__":
    unittest.main()
