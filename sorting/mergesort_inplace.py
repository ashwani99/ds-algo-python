def merge_sort(arr):
    n = len(arr)
    return _merge_sort(arr, 0, n-1)


def _merge_sort(arr, start, end):
    if start < end:
        mid = (start+end)//2
        _merge_sort(arr, start, mid)
        _merge_sort(arr, mid+1, end)
        _merge(arr, start, mid, end)
    return arr


def _merge(arr, start, mid, end):
    left = start
    right = mid+1

    # if already sorted
    if arr[mid] <= arr[right]:
        return

    while left <= mid and right <= end:
        if arr[left] < arr[right]:
            left += 1
        else:
            index = right
            value = arr[right]
            while index != left:
                arr[index] = arr[index-1]
                index -= 1
            arr[left] = value
            left += 1
            mid += 1
            right += 1


if __name__ == '__main__':
    print(merge_sort([9, 7, 8, 3, 2, 10, 1, 7]))
