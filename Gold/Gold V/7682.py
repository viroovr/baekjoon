def find_winstate(state):
    # 0,1,2 가로 3,4,5세로, 6,7 -45도 대각선, 45도 대각선
    win_state = [None] * 8

    for i in range(0,9,3):
        if state[i] != "." and state[i] == state[i+1] and state[i+1] == state[i+2]:
            win_state[i // 3] = state[i]

    for i in range(3):
        if state[i] != "." and state[i] == state[i + 3] and state[i + 3] == state[i + 6]:
            win_state[3 + i] = state[i]
    
    if state[0] != "." and state[0] == state[4] and state[4] == state[8]:
        win_state[6] = state[0]
    if state[2] != "." and state[2] == state[4] and state[4] == state[6]:
        win_state[7] = state[2]
    
    return win_state

def is_possible_state(state):
    x_cnt = state.count("X")
    o_cnt = state.count("O")
    if x_cnt < 3:
        return False
    
    res = False
    if x_cnt == o_cnt:
        win_state = find_winstate(state)
        if win_state.count("O") == 1 and win_state.count("X") == 0:
            res = True
    elif x_cnt == o_cnt + 1:
        win_state = find_winstate(state)
        x_win, o_win = win_state.count("X"), win_state.count("O")
        if x_cnt < 5:
            if x_win == 1 and o_win == 0:
                res = True
        else:
            if (x_win <= 2 and o_win == 0):
                res = True
    
    return res


def sol():
    result = []
    while True:
        state = list(input())
        if state[0] == "e":
            break
        if is_possible_state(state):
            result.append("valid")
        else:
            result.append("invalid")
    
    print("\n".join(result))

sol()