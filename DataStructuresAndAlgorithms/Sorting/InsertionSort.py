#! /usr/bin/env python3

def insertion_sort(arr):
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                temp = arr[j - 1]
                arr[j - 1] = arr[j]
                arr[j] = temp
    return arr


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(insertion_sort(arr))
