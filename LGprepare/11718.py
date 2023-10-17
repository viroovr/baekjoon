str_list = []
for _ in range(100):
    try:
        k = input()
        if not k:
            break
        str_list.append(k)
    except EOFError:
        break
for s in str_list:
    print(s)
