def quick_sort(arr, start, end):
    if start <= end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot-1)
        quick_sort(arr, pivot+1, end)
    return arr


def partition(arr, start, end):
    pivot = start
    boundary = start+1
    for j in range(boundary, end+1):
        if arr[j] < arr[pivot]:
            arr[boundary], arr[j] = arr[j], arr[boundary]
            boundary += 1
    arr[pivot], arr[boundary-1] = arr[boundary-1], arr[pivot]
    return boundary-1


if __name__ == '__main__':
    print(quick_sort([9, 7, 8, 3, 2, 10, 1], 0, 6))

