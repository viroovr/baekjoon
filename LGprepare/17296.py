def find_NGE(cur_index):
    for i in range(cur_index + 1, N):
        if seq[i] > seq[cur_index]:
            return seq[i]
    return -1


def main():
    global seq, N, ans
    N = int(input())
    seq = list(map(int, input().split()))
    ans = [find_NGE(0)]
    for cur_index in range(1, N):
        prev_nge, prev_num = ans[cur_index - 1], seq[cur_index - 1]
        cur_num = seq[cur_index]
        if prev_nge == -1:
            if prev_num > cur_num:
                ans.append(cur_index)
            else:
                ans.append(-1)
        else:
            if prev_num > cur_num:
                ans.append(prev_nge)
    

    # seq = [i for i in range(1_0000, 0, -1)]


    # for i in range(N):
    #     find_nge = False
    #     for j in range(i + 1, N):
    #         if seq[j] > seq[i]:
    #             find_nge = True
    #             ans.append(seq[j])
    #             break
    #     if not find_nge:
    #         ans.append(-1)
    # print(ans)


