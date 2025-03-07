"""
1. DP 갱신 방식 변경 (Bottom-up)
    - length를 3 이상부터 처리하면서 dp[start][end] = dp[start+1][end-1] 확인
    - numbers[start] == numbers[end] 조건을 먼저 체크하여 불필요한 연산 방지
2. 시간 단축:
    - 원래 코드에서 dp[start+1][end-1]을 확인할 때 매번 if 검사를 수행
    - numbers[start] == numbers[end] 먼저 확인 후 dp[start+1][end-1]을 확인하여 불필요한 연산을 줄임
3. 출력 최적화 (sys.stdout.write)
    - print()는 호출될 때마다 I/O 연산을 발생시키므로 속도가 느림
    - 문자열을 한꺼번에 sys.stdout.write()로 출력하여 실행 속도 단축
4. 인풋 최적화
    - sys.stdin.readline
188688	1944    4
248016	1740    2,3,4
248048	1692    1,2,3,4
"""
import sys
input = sys.stdin.readline

def answer_palindrome(numbers, questions):
    dp = [[0] * N for _ in range(N)]
    
    for i in range(N):
        dp[i][i] = 1

    for i in range(N - 1):
        if numbers[i] == numbers[i + 1]:
            dp[i][i + 1] = 1

    for length in range(3, N + 1):
        for start in range(N - length + 1):
            end = start + length - 1
            
            if numbers[start] == numbers[end] and dp[start + 1][end - 1]:
                dp[start][end] = 1
    
    output = []
    for s, e in questions:
        output.append(str(dp[s][e]))
    sys.stdout.write("\n".join(output) + "\n")
                
N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
questions = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
answer_palindrome(numbers, questions)