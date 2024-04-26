N = int(input())
SERIES = '666'
FIRST = 6
SECOND = 10
count = -1
index = 0


def count_range_and_end(prefix, fromm, to):
    global index
    for i in range(fromm, to):
        index += 1
        if index == N:
            print(int(prefix + str(i) + SERIES))
            return True
    return False


def redundant_prefix_and_count(prefix, pop_num):
    global index
    for _ in range(pop_num):
        prefix.pop()
    prefix = "".join(prefix)
    for i in range(10 ** (pop_num + 1)):
        index += 1
        if index == N:
            print(int(prefix + SERIES + '0' * ((pop_num + 1) - len(str(i))) + str(i)))
            return True
    return False


def solution():
    global count, index
    while True:
        count += 1
        prefix = '00' + str(count)
        if count_range_and_end(prefix, 0, FIRST):
            return
        if prefix[-1] != '6':
            if redundant_prefix_and_count(list(prefix), 0):
                return
        elif prefix[-2] != '6':
            if redundant_prefix_and_count(list(prefix), 1):
                return
        elif prefix[-3] != '6':
            if redundant_prefix_and_count(list(prefix), 2):
                return
        elif prefix[-3] == '6':
            if redundant_prefix_and_count(list(prefix), 3):
                return
        if count_range_and_end(prefix, FIRST + 1, SECOND):
            return


solution()
