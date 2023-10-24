from string import ascii_lowercase
str2num = {s: i for i, s in enumerate("0123456789" + ascii_lowercase)}


def solution():
    N, B = input().split()
    N = N.lower()
    B = int(B)
    answer = 0
    for num_order, char in enumerate(reversed(N)):
        answer += str2num[char] * (B ** num_order)
    return answer


print(solution())
