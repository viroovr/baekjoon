def quick_sort(array: list, start, end):
    if end <= start:
        return
    pivot = array[start]
    i, j = start + 1, end
    while i <= j:
        while i <= end and array[i] <= pivot:
            i += 1
        while start < j and array[j] >= pivot:
            j -= 1
        if i < j:
            array[i], array[j] = array[j], array[i]
        else:
            array[start], array[j] = array[j], array[start]
    quick_sort(array, start, i - 1)
    quick_sort(array, j + 1, end)
    return array


if __name__ == "__main__":
    print(quick_sort([5, 7, 9, 0, 3, 1, 6, 2, 4, 8], 0, 9))
