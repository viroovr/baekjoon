"""
s 길이의 약수들을 구하고 이 약수만큼의 패턴이 * 연산으로 s와 일치하는지 확인했다.
s길이 만큼 약수를 전부 찾지 않고 1을 제외한 가장 작은 약수는 2 이므로 절반까지만 확인하도록 하니까
시간 통과 됐다.

그런데 리스트 슬라이싱에 의한 비교는 시간초과가 난다.

하지만, 이 문제는 KMP의 failure function(LPS(Longest Prefix which is also Suffix))로 풀도록 권장된다.
KMP학습이 목적이기 때문에 KMP로도 참고해서 풀어봤다.
36316	828     * 연산
115428	1980    LPS
"""
def compute_lps(s):
    N = len(s)
    j = 0
    lps = [0] * N
    for i in range(1, N):
        while j > 0 and s[i] != s[j]:
            j = lps[j - 1]
        
        if s[i] == s[j]:
            j += 1
            lps[i] = j
    return lps

def sol():
    while True:
        s = input()
        if s == '.':
            break
        
        lps = compute_lps(s)
        length = len(s)
        pattern_length = length - lps[-1]
        if length % pattern_length == 0:
            print(length // pattern_length)
        else:
            print(1)
    
sol()