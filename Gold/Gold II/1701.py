"""
N이 5000을 N^2도 꽤 빠를 수 있다 생각했다.
brute forth로 했지만, 모든 경우를 탐색하는 것은 리스트슬라이싱과 해싱 등에서 시간초과가 발생했다.

어떤 길이의 substring에서 반복되는 문자열이 발견되면, 더 작은 길이에서는 볼 필요없고
더 큰 길이에서 발견될 가능성이 있으므로, 이를 이분탐색으로 해결할 아이디어를 얻었다.

gpt는 Suffix Array와 LCP를 섞은 풀이를 알려줬는데, 아직 잘 이해가 안된다.
내가 생각해서 푼게 아니라 그런듯

37820	60
"""

def get_longest_length(T:str):
    N = len(T)
    left, right = 1, N - 1
    res = 0
    while left <= right:
        length = (left + right) // 2
        dict = set()
        for start in range(N - length + 1):
            key = T[start:start + length]
            if key in dict:
                res = length
                break
            dict.add(key)
        else:
            right = length - 1
            continue
        left = length + 1

    return res

def sol():
    T = input()
    print(get_longest_length(T))

sol()