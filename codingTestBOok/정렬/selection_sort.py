def selection_sort(array):
    for i in range(len(array)):
        swap = i
        min_num = array[i]
        for j in range(i + 1, len(array)):
            if array[j] < min_num:
                min_num = array[j]
                swap = j
        array[i], array[swap] = array[swap], array[i]
    return array
