class Solution():
    N = 0
    K = 0
    time = 0

    def __init__(self) -> None:
        self.N, self.K = map(int, input().split())
        self.time = 0

    def main(self):
        k, n = self.K, self.N
        if k <= n:
            print(n - k)
            return
        min_time = 1_000_001
        count = 0
        if n == 0:
            n = 1
            self.time += 1
        while k != n:
            if 2 * n <= k:
                n *= 2
                self.time += 1
            elif k < 2 * n:
                # temp_min = min(count + 1 + abs(2 * n - k), count + k - n)
                # while min_time > temp_min and n > 0:
                #     print(k, n, temp_min, min_time)
                #     min_time = temp_min
                #     count += 1
                #     n -= 1
                #     temp_min = min(count + 1 + abs(2 * n - k), count + k - n)
                # else:
                #     self.time += min_time
                #     n = k
                if k % 2 == 0:
                    self.time += min(k - n, 1 + n - k // 2)
                else:
                    u = int(n - k / 2)
                    compList = [k - n, 2 * n - u - k + 1,
                                3 * (u + 1) - 2 * n - k + 1]
                    print(u, compList)
                    self.time += min([x for x in compList if x >= 0])

                break

        print(self.time)


sol = Solution()
sol.main()
