while True:
    try:
        n = int(input())
        if not n:
            print("not n")
            break
    except (EOFError, ValueError):
        break
    i = 1
    k = 1
    while True:
        if k % n == 0:
            break
        else:
            k *= 10
            k += 1
            i += 1
    print(i)
