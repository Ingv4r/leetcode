def sort_square(array):
    if not array:
        return array
    res = [None for i in range(len(array))]
    left, right, pos = 0, len(array) - 1, -1
    while right > left:
        left_num = array[left] ** 2
        right_num = array[right] ** 2
        if left_num > right_num:
            res[pos] = left_num
            left += 1
            pos -= 1
        elif right_num > left_num:
            res[pos] = right_num
            right -= 1
            pos -= 1
        elif left_num == right_num:
            res[pos] = right_num
            res[pos - 1] = right_num
            left += 1
            right -= 1
            pos -= 2
    res[0] = array[left] ** 2
    return res


