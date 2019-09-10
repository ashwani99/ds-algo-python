def binary_search(sorted_arr, key):
    return _binary_search(sorted_arr, 0, len(sorted_arr)-1, key)


def _binary_search(arr, start, end, key):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            end = mid-1
        else:
            start = mid+1
    return None


if __name__ == '__main__':
    # arr needs to be sorted
    arr, key = [1, 2, 3, 4, 6, 9, 30, 77, 90], 9
    index = binary_search(arr, key)
    if index:
        print('{} found at index {}'.format(key, index))
    else:
        print('{} not found in the array'.format(key))

