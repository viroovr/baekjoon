def main():
    N, M = map(int, input().split())
    po2num = {str(i + 1): input() for i in range(N)}
    num2po = {v: i for i, v in po2num.items()}
    given = [input() for _ in range(M)]
    for st in given:
        if st in po2num:
            print(po2num[st])
        else:
            print(num2po[st])


main()
