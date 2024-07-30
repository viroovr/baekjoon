from random import shuffle


def get_random_array(N):
    print("array length :", N)
    array = [i for i in range(N)]
    shuffle(array)
    return array
