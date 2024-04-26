class Solution():
    N, L = 0, 0
    partial_sum_list = []

    def __init__(self) -> None:
        self.N, self.L = map(int, input().split())

    def main(self):
        self.set_partial_sum()

        # print(self.partial_sum_list)

    def set_partial_sum(self):
        for n in range(1000000):
            t = (n * (n + 1)) // 2
            if t < 1_000_000_000:
                self.partial_sum_list.append(t)
            else:
                break


sol = Solution()
sol.main()
