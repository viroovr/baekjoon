from string import ascii_uppercase
letters = [str(x) for x in range(10)]
letters.extend([x for x in list(ascii_uppercase)])


def solution():
    N, B = map(int, input().split())
    temp = N
    ans = []

    while temp // B != 0:
        ans.append(temp % B)
        temp //= B
    ans.append(temp)
    print("".join([letters[ans[i]] for i in range(len(ans) - 1, -1, -1)]))


solution()
