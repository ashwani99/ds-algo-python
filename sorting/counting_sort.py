def counting_sort(arr):
    frequencies = [0]*(max(arr)+1)
    for number in arr:
        frequencies[number] += 1

    sorted_arr = []
    for number, count in enumerate(frequencies):
        sorted_arr.extend([number]*count)

    return sorted_arr


if __name__ == '__main__':
    print(counting_sort([9, 7, 8, 3, 2, 3, 10, 1]))
