# You are given an unordered array consisting of consecutive integers
# [1, 2, 3, ..., n] without any duplicates.
# You are allowed to swap any two elements.
# You need to find the minimum number of swaps required to sort the array in ascending order.


def minimumSwaps(arr):
    count = 0
    for idx1, ele in enumerate(arr):
        print(idx1)
        if idx1 != ele - 1:
            for idx2, ele2 in enumerate(arr):
                if ele2 - 1 == idx1:
                    swap(arr, idx1, idx2)
                    count += 1
                    break
    return count


def swap(arr, idx, idx2):
    tmp = arr[idx]
    arr[idx] = arr[idx2]
    arr[idx2] = tmp
