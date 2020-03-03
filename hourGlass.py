def hourglassSum(arr):
    row_size = len(arr)
    col_size = len(arr[0])
    max_sum = None
    for i in range(row_size - 2):
        for j in range(col_size - 2):
            starting_point = arr[i][j]
            sum = 0
            for add_i in range(3):
                for add_j in range(3):
                    if (add_i == 1 or add_j != 1):
                        sum += arr[i + add_i][j + add_j]

            if (max_sum is None or max_sum < sum):
                max_sum = sum

    return max_sum


arr = [[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 1, 2, 4, 0]]
