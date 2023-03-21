from time import perf_counter
import tracemalloc
tracemalloc.start()

def write_db(db:dict, file_name):
    with open(file_name + '.txt', "w") as f:
        f.write('')

    with open(file_name + '.txt', "a") as f:
        for k, v in db.items():
            f.write(f"{k} {v['full_name']} {v['email']} {v['major']}\n")

def performance_counter_decorator(func):
    def count(*args, **kwargs):
        tracemalloc.reset_peak()
        start = perf_counter()
        re = func(*args, **kwargs)
        stop = perf_counter()
        memory = tracemalloc.take_snapshot()
        peaks = tracemalloc.get_traced_memory()
        return (stop - start, (memory, peaks[1]), re)

    return count

def bubble_sort(array:list):
    arr = array.copy()
    length = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, length):
            if arr[i-1] > arr[i]:
                temp = arr[i-1]
                arr[i-1] = arr[i]
                arr[i] = temp
                swapped = True

    return arr

def insertion_sort(array:list):
    arr = array.copy()
    i = 1
    while i < len(arr):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            j -= 1
        i += 1

    return arr


def selection_sort(array:list):
    temp = []
    arr = array.copy()
    while len(temp) < len(array):
        min = (arr[0], 0)
        for j, i in enumerate(arr):
            if i < min[0]:
                min = (i, j)
        temp.append(min[0])
        arr.pop(min[1])

    return temp

def merge_sort(array):
    if len(array) <= 1:
        return array

    left: dict = array[:len(array)//2]
    right = array[len(array)//2:]

    left = merge_sort(left)
    right = merge_sort(right)
    
    temp = []
    while len(left) and len(right):
        if left[0] <= right[0]:
            temp.append(left[0])
            left = left[1:]
        else:
            temp.append(right[0])
            right = right[1:]

    while len(left):
        temp.append(left.pop(0))
    while len(right):
        temp.append(right.pop(0))

    return temp

@performance_counter_decorator
def id_sort(d: dict, func):
    array = []
    temp = {}
    for i in d:
        array.append(i)
    
    array = func(array)
    for i in array:
        temp[i] = d.get(i)

    # write_db(temp, "id_" + func.__name__)

    return temp

@performance_counter_decorator
def fn_sort(d: dict, func):
    array = []
    temp = {}
    for i in d.values():
        array.append(i['first_name'])
    
    array = func(array)
    for i in array:
        for k, v in d.items():
            if v['first_name'] == i:
                temp[k] = v
                break
        
    # write_db(temp, "fn_" + func.__name__)

    return temp