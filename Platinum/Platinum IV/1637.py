"""
최적화 문제를 매개변수 탐색으로 변경해서 푸는 문제이다.
근데 이게 매개변수 탐색이 가능한지를 아는게 더 어려운것 같다.
많이 풀어보면서 감을 잡아야겠다. gpt도 최적화로 품
35480	192
"""
import sys
input = sys.stdin.readline
def count(number):
    cnt = 0
    for i in range(N):
        check_num = min(numbers[i][1], number)
        if check_num < numbers[i][0]:
            temp = 0
        else:
            temp = (check_num - numbers[i][0]) // numbers[i][2] + 1
        cnt += temp
    return cnt

def get_odd_number():
    left, right = 1, 2_147_483_647
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if count(mid) % 2 == 1:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    if result:
        cnt = count(result) - count(result - 1)
        print(*[result, cnt])
    else:
        print("NOTHING")

def sol():
    global N, numbers
    N = int(input())
    numbers = [tuple(map(int, input().rstrip().split())) for _ in range(N)]

    get_odd_number()

sol()    