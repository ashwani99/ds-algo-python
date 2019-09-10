def binary_search(sorted_arr, key):
    return _binary_search(sorted_arr, 0, len(sorted_arr)-1, key)


def _binary_search(arr, start, end, key):
    if start <= end:
        mid = (start+end)//2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            return _binary_search(arr, start, mid, key)
        else:
            return _binary_search(arr, mid+1, end, key)
    return None


if __name__ == '__main__':
    # arr needs to be sorted
    arr, key = [1, 2, 3, 4, 6, 9, 30, 77, 90], 99
    index = binary_search(arr, key)
    if index:
        print('{} found at index {}'.format(key, index))
    else:
        print('{} not found in the array'.format(key))

