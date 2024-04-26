class Solution():
    N = 0
    K = 0
    shop_vase = 0
    vase_index = 0
    vase_count = [0 for _ in range(30)]

    def __init__(self) -> None:
        self.N, self.K = map(int, input().split())

    def main(self):
        temp_vase_num = self.N
        vase_count_num = 1
        while temp_vase_num > 1:
            self.vase_count[self.vase_index] = temp_vase_num % 2
            self.vase_index += 1
            temp_vase_num //= 2
            vase_count_num += 1
        self.vase_count[self.vase_index] = temp_vase_num

        while self.vase_count.count(1) > self.K:
            u = self.vase_count.index(1)
            self.shop_vase += 2 ** u
            self.vase_count[u] = 0
            carry = 1
            while carry == 1:
                self.vase_count[u + 1] += carry
                carry = 0
                if self.vase_count[u + 1] == 2:
                    self.vase_count[u + 1] = 0
                    u = u + 1
                    carry = 1

        print(self.shop_vase)
        # print(vase_count_num)
        # print(self.vase_count)


sol = Solution()
sol.main()

# 3 1
# 2 1 1
# 2 2
# 4

# 13 2
# 2 2 2 2 2 2 1
# 4 4 4 1
# 8 4 1 1 1 1
# 8 4 4
# 16
