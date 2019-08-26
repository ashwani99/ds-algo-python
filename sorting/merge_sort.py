def merge_sort(arr):
    l = len(arr)
    return _merge_sort(arr, 0, l-1)


def _merge_sort(arr, start, end):
    if start < end:
        mid = (start+end)//2
        _merge_sort(arr, start, mid)
        _merge_sort(arr, mid+1, end)
        merge(arr, start, mid, end)
    return arr


def merge(arr, start, mid, end):
    result = []
    left = start
    right = mid+1
    
    # compare and fill while both left and right array are not empty
    while left <= mid and right <= end:
        if arr[left] <= arr[right]:
            result.append(arr[left])
            left += 1
        else:
            result.append(arr[right])
            right += 1

    # if left has some left put all in result
    while left <= mid:
        result.append(arr[left])
        left += 1

    # if right has some left put all in result
    while right <= end:
        result.append(arr[right])
        right += 1

    # replacing values into the original array
    for i in range(len(result)):
        arr[i+start] = result[i]


if __name__ == '__main__':
    print(merge_sort([5, 4, 3, 2, 1, -9, 5, 3]))
