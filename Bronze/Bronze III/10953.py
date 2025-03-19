"""
데이터 입력 처리
32412	32
"""
import sys
data = sys.stdin.read().split()
T = int(data[0])
result = []
for i in range(1, T + 1):
    A,B=map(int,data[i].split(","))
    result.append(f"{A + B}\n")
sys.stdout.write("".join(result))