"""
인덱스로 풀었다가 당연히 시간초과 예상하고 제출. 당연히 시간 초과
리스트 슬라이싱을 이용한 분할정복으로 풀었다가 메모리 초과.
리스트 글로벌로 설정하고 O(n) 으로 최소 높이 찾는 분할 정복 사용했다가 시간초과.
세그먼트 트리를 활용했다는 질문 게시판 보고, 사용했는데 시간 초과.
gpt한테 물어봐서 스택을 사용해 O(n)의 시간복잡도 방법 알고 제출 통과.

스택 풀이 분석
1. 시간 복잡도 분석
    각 직사각형은 최대 두 번 스택에서 처리됨:
    한 번 push
    한 번 pop
    따라서 총 연산 횟수 = O(n).

2. 최악의 경우에도 O(n) 유지되는 이유
    내림차순 입력 (5 4 3 2 1)
    각 숫자가 들어올 때마다 pop이 발생하지만, 각 숫자는 한 번만 push & pop → O(n).
    오름차순 입력 (1 2 3 4 5)
    pop이 마지막에 몰아서 발생하지만, 각 숫자는 한 번만 push & pop → O(n).
    즉, 모든 경우에 대해 한 번 push, 한 번 pop 되므로 최대 2n 연산 → O(n)!
"""

def get_largest_rectangle():
    st = []
    max_area = 0
    for i in range(N):
        while st and hisograms[st[-1]] > hisograms[i]:
            height = hisograms[st.pop()]
            width = i if not st else i - st[-1] - 1
            max_area = max(max_area, width * height)
        st.append(i)

    while st:
        height = hisograms[st.pop()]
        width = N if not st else (N - st[-1] - 1)
        max_area = max(max_area, height * width)
    
    return max_area

def sol():
    global N, hisograms, tree
    while True:
        line = list(map(int, input().split()))
        if line[0] == 0:
            return
        
        N, hisograms = line[0], line[1:]
        # print(tree)
        print(get_largest_rectangle())
    
sol()