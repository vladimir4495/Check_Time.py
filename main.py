import random
import time

class ChekTime:
    def __enter__(self):
        self.begin = time.time()
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f" отработала {time.time() - self.begin}")



def check_time(func):
    def func_2(*args, **kwargs):
        timestart = time.time()
        c = func(*args, **kwargs)
        print(f"{func.__name__} отработала {time.time() - timestart}")
        return c

    return func_2



def marsort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    left = arr[0:len(arr) // 2]
    right = arr[len(arr) // 2:]
    left_sorted = marsort(left)
    right_sorted = marsort(right)
    result = []
    while left_sorted and right_sorted:
        if left_sorted[0] > right_sorted[0]:
            result.append(right_sorted.pop(0))
        else:
            result.append(left_sorted.pop(0))

    result.extend(left_sorted)
    result.extend(right_sorted)
    return result


@check_time
def bublesort(arr: list[int]) -> list[int]:
    flag = True
    while flag:
        coun = 0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                coun += 1
        if coun == 0:
            flag = False
    return arr


if __name__ == '__main__':
    print(marsort([2, 5, 3, 8, 33, 21, 12]))

    print(bublesort([2, 5, 3, 8, 33, 21, 12]))
    arr = []
    arr1 = []
    for i in range(0, 10000):
        arr.append(random.randint(0, 30000000))
        arr1.append(random.randint(0, 30000000))
    print("go sorted")
    with ChekTime():
        marsort(arr)
    bublesort(arr1)