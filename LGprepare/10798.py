N = 5
letters = [input() for _ in range(N)]
for i in range(max(len(x) for x in letters)):
    case = []
    for k in letters:
        try:
            case.append(k[i])
        except IndexError:
            continue
    print("".join(case), end="")
print()
