class Mash():
    width = 0
    height = 0
    box = None
    directionNWSE = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    unripen_list = []

    unripen_tomatoes = 0
    total_ripening_tomato = 0

    def __init__(self) -> None:
        self.width, self.height = map(int, input().split())
        self.box = [list(map(int, input().split()))
                    for _ in range(self.height)]
        # self.width, self.height = 1000, 1000
        # self.box = [[1 for _ in range(self.width)]
        #             for _ in range(self.height)]

    def get_box(self):
        return self.box

    def find_ripen_tomato_and_unripen_tomato_number(self):
        pos_tomato = []
        for y in range(self.height):
            for x in range(self.width):
                if self.box[y][x] == 1:
                    pos_tomato.append((x, y))
                elif self.box[y][x] == 0:
                    self.unripen_tomatoes += 1
        return pos_tomato

    def get_side_of_ripen_tomato_and_ripen(self):
        return_list = []
        for ripe_pos in self.unripen_list:
            x, y = ripe_pos
            for dx, dy in self.directionNWSE:
                X, Y = x + dx, y + dy
                if (self.is_in_box(X, Y) and self.is_unripen(X, Y)):
                    self.box[Y][X] = 1
                    return_list.append((X, Y))
        self.total_ripening_tomato += len(return_list)
        self.unripen_list = return_list

    def is_in_box(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def is_unripen(self, x, y):
        return self.box[y][x] == 0

    def is_end(self):
        return self.total_ripening_tomato == self.unripen_tomatoes


class Solution():
    mash = None
    day_elapsed = 0

    def __init__(self) -> None:
        self.mash = Mash()
        self.is_end_bool = False

    def increment_day(self):
        self.day_elapsed += 1

    def ripen_tomato(self):
        self.setting_tomato()
        if self.mash.unripen_list:
            self.increment_day()
        else:
            self.is_end_bool = True

    def setting_tomato(self):
        if self.day_elapsed == 0:
            self.mash.unripen_list = self.mash.find_ripen_tomato_and_unripen_tomato_number()
        self.mash.get_side_of_ripen_tomato_and_ripen()

    def is_end(self):
        if self.is_end_bool:
            if not self.mash.is_end():
                self.day_elapsed = -1
            return True
        return False


sol = Solution()

# start = time.time()
while not sol.is_end():
    sol.ripen_tomato()
else:
    print(sol.day_elapsed)
# end = time.time()
# print("Elapsed time: ", end - start)
