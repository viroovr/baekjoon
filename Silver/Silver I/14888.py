"""
개선된 점
중복 제거:
    set(permutations(...))을 사용하지 않고 백트래킹을 사용해 중복되는 경우를 제거.
메모리 절약:
    permutations()을 사용하면 최대 10! = 3,628,800개 생성, 백트래킹은 불필요한 경우를 미리 가지치기해서 메모리 절약.
빠른 연산:
    재귀를 활용하여 연산을 그때그때 수행하므로 별도로 수식을 저장할 필요 없음.

연산자의 최대 개수는 10! (≈ 3.6M)이지만, 백트래킹을 사용하면 최대 4^10 = 1,048,576번의 연산만 수행.
최악의 경우에도 O(4^N) ≈ O(1M)이므로 충분히 해결 가능!

알고리즘    메모리(KB)  시간(ms)    
브루트포스  38556       496
백트랙킹    32412       64
"""
def operate(a, b, op):
    if op == 0:
        return a + b
    elif op == 1:
        return a - b
    elif op == 2:
        return a * b
    elif op == 3:
        return a // b if a >= 0 else -((-a) // b)

def backtrack(depth, total, operators):
    global max_value, min_value
    if depth == n - 1:
        max_value = max(max_value, total)
        min_value = min(min_value, total)
        return
    
    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            backtrack(depth + 1, operate(total, numbers[depth + 1], i), operators)
            operators[i] += 1
        
def sol():
    global n, numbers, max_value, min_value
    n = int(input())
    numbers = list(map(int, input().split()))
    operators = list(map(int, input().split()))

    max_value = -10 ** 9
    min_value = 10 ** 9

    backtrack(0, numbers[0], operators)

    print(max_value)
    print(min_value)

if __name__ == "__main__":
    sol()