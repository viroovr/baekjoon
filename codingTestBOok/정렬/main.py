from insertion_sort import insertion_sort
from selection_sort import selection_sort
from quick_sort import quick_sort
from count_sort import count_sort
from time import time
from randomarray import get_random_array
N = 1000


def timing(sorting, fun, show_array=False):
    start = time()
    if fun == "quick":
        ret_array = sorting(get_random_array(N), start=0, end=N - 1)
    else:
        ret_array = sorting(get_random_array(N))
    end = time()
    if show_array:
        print("returned array: ", ret_array)
    print(fun, "sorting array : ", end - start, "sec")


timing(selection_sort, "selection")
timing(insertion_sort, "insertion")
timing(quick_sort, "quick")
timing(count_sort, "count", True)
