def longestPeak(array):
    # Write your code here.
    max_peak = 0
    for i in range(len(array)):
        if is_peak(array, i):
            print(i)
            curr_len = calc_length(left_stop(array, i), right_stop(array, i))
            if curr_len > max_peak:
                max_peak = curr_len
    return max_peak


def is_peak(array, i):
    if i <= 0 or i >= len(array) - 1:
        return False
    return array[i - 1] < array[i] and array[i + 1] < array[i]


def left_stop(array, i):
    while i >= 1 and array[i - 1] < array[i]:
        i -= 1
    return i


def right_stop(array, i):
    while i < len(array) - 1 and array[i + 1] < array[i]:
        i += 1
    return i


def calc_length(i, j):
    return j - i + 1


if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1, 2, 1]
    print(longestPeak(arr))
