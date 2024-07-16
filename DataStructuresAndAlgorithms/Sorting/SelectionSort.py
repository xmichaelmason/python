#! /usr/bin/env python3

def selection_sort(arr):
    for i in range(len(arr)):
        idx = i
        for j in range(i, len(arr)):
            if arr[j] < arr[idx]:
                idx = j

        temp = arr[i]
        arr[i] = arr[idx]
        arr[idx] = temp

    return arr


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(selection_sort(arr))
