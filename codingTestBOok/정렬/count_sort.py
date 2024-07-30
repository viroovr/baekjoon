def count_sort(array: list):
    counting_array = [0] * (max(array) + 1)
    for i in array:
        counting_array[i] += 1
    new_array = []
    for i in range(len(counting_array)):
        new_array.extend([i] * counting_array[i])
    return new_array


if __name__ == "__main__":
    print(count_sort([7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]))
