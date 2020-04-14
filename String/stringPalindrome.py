def Solution(arr):
    string_len = len(arr)
    for i in range(0, len(s) // 2):
        if arr[i] != arr[string_len - i - 1]:
            printnow(False)
            return

    printnow(True)


def printnow(result):
    if result == True:
        print("TRUE")
    else:
        print("FALSE")


s = "aman is si nama"

Solution(s)
