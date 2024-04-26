class Solution():
    N = 0
    mat = None

    def __init__(self) -> None:
        # pass
        self.N = int(input())
        self.mat = [[0 for _ in range(10)] for _ in range(10)]
        for i in range(1, 10):
            for j in range(i, 10):
                self.mat[i][j] = [k for k in range(i-1, j)]

    def __main__(self):
        count_number_mat = [[1 for _ in range(10)] for _ in range(10)]
        for i in range(1, 10):
            for j in range(1, 10):
                if isinstance(self.mat[i][j], list):
                    count_number_mat[i][j] = sum(
                        [count_number_mat[i - 1][x] for x in self.mat[i][j]])
        counter = 9
        if 0 <= self.N <= 9:
            print(self.N)
            return
        else:
            y, x = self.calculate_counter(count_number_mat)
            print(y, x)
        # print(self.mat)
        # print(count_number_mat)

    def calculate_counter(self, counting_list):
        counter = 0
        for i in range(1, 10):
            for j in range(1, 10):
                counter += counting_list[i][j]
                if counter >= self.N:
                    return (i, j)


# [[0,1,2,3,4,5,6,7,8,9],
#  [0,[0], [0, 1], [0,1,2], [...], [0,1,2,3,4,5,6,7,8]],
#  [0, 0, [1], [1,2], [1,2,3], [1,2,3,4], ... [1,2,3,4,5,6,7,8]]
#  ]

# [[0,1,2,3,4,5,6,7,8,9],
#  [0,1, 2, 3, [...], 8],
#  [0, 0, 1, 3, 6, 10, 15, 21, 28, 36]
#  ]

# [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0,
#   [0],
#   [0, 1],
#   [0, 1, 2],
#   [0, 1, 2, 3],
#   [0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4, 5],
#   [0, 1, 2, 3, 4, 5, 6],
#   [0, 1, 2, 3, 4, 5, 6, 7],
#   [0, 1, 2, 3, 4, 5, 6, 7, 8]],
#  [0,
#   0,
#   [1],
#   [1, 2],
#   [1, 2, 3],
#   [1, 2, 3, 4],
#   [1, 2, 3, 4, 5],
#   [1, 2, 3, 4, 5, 6],
#   [1, 2, 3, 4, 5, 6, 7],
#   [1, 2, 3, 4, 5, 6, 7, 8]],
#  [0,
#   0,
#   0,
#   [2],
#   [2, 3],
#   [2, 3, 4],
#   [2, 3, 4, 5],
#   [2, 3, 4, 5, 6],
#   [2, 3, 4, 5, 6, 7],
#   [2, 3, 4, 5, 6, 7, 8]],
#  [0,
#   0,
#   0,
#   0,
#   [3],
#   [3, 4],
#   [3, 4, 5],
#   [3, 4, 5, 6],
#   [3, 4, 5, 6, 7],
#   [3, 4, 5, 6, 7, 8]],
#  [0, 0, 0, 0, 0, [4], [4, 5], [4, 5, 6], [4, 5, 6, 7], [4, 5, 6, 7, 8]],
#  [0, 0, 0, 0, 0, 0, [5], [5, 6], [5, 6, 7], [5, 6, 7, 8]],
#  [0, 0, 0, 0, 0, 0, 0, [6], [6, 7], [6, 7, 8]],
#  [0, 0, 0, 0, 0, 0, 0, 0, [7], [7, 8]],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, [8]]]
sol = Solution()
sol.__main__()
