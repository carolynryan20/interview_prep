import math

def increment_array(arr):
    if not arr:
        return arr

    # print("Original Array",arr)
    for i in range(len(arr) -1, -1, -1):
        if arr[i] + 1 > 9:
            arr[i] = 0
        else:
            arr[i] += 1
            break


    for item in arr:
        if item != 0:
            # print("Return arr", arr)
            return arr

    # print("Return arr", [1]+arr)
    return [1] + arr

def increment_array_n(n, arr):
    for i in range(n):
        arr = increment_array(arr)
    return arr

def increment_arr_n_with_log(n, arr):
    str_n = str(n)

    while len(arr) < len(str_n):
        # Make array longer
        arr = [0] + arr

    str_index = 0
    for i in range(len(str_n)-1, -1, -1):
        new_n = int(str_n[str_index])
        if i == 0:
            internal_arr = arr
            next_arr = []
        else:
            internal_arr = arr[:-i]
            next_arr = arr[-i:]
        print("Increment_n({}, {})".format(new_n, internal_arr))
        arr = increment_array_n(new_n, internal_arr) + next_arr
        print("Incremented array", arr)
        str_index += 1

    return arr







if __name__ == '__main__':
    # increment_arr_n_with_log(123, [4,5,6,7])
    #
    # arr = [1,2,3,4]
    # assert (increment_array(arr) == [1,2,3,5])
    #
    # arr = [1,0,9,9]
    # assert (increment_array(arr) == [1,1,0,0])
    #
    # arr = [9,9]
    # assert (increment_array(arr) == [1,0,0])
    #
    # arr = [1]
    # assert (increment_array(arr) == [2])
    #
    # arr = []
    # assert (increment_array(arr) == [])
    #
    #
    arr = [1, 2, 3, 4]
    assert (increment_arr_n_with_log(4, arr) == [1, 2, 3, 8])

    arr = [1, 0, 9, 9]
    assert (increment_arr_n_with_log(20, arr) == [1, 1, 1, 9])

    arr = [9, 9]
    assert (increment_arr_n_with_log(1000, arr) == [1, 0, 9, 9])

    arr = [4,5,6,7]
    assert (increment_arr_n_with_log(123, arr) == [4,6,9,0])

    arr = [1]
    assert (increment_arr_n_with_log(10, arr) == [1,1])

    arr = []
    assert (increment_arr_n_with_log(0, arr) == [0])