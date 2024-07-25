#! /usr/bin/env python3
def bubble_sort(arr):
    for i in range(len(arr) - 1 - i):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    print(bubble_sort(arr))
