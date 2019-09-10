# ternary search is also used to find the minimum or maximum value of a unimodal function
# read more here https://www.hackerearth.com/practice/algorithms/searching/ternary-search/tutorial/

def ternary_search(sorted_arr, key):
    return _ternary_search(sorted_arr, 0, len(sorted_arr)-1, key)


def _ternary_search(arr, start, end, key):
    while start <= end:
        separator1 = start + (end-start)//3
        separator2 = end - (end-start)//3

        if arr[separator1] == key:
            return separator1
        if arr[separator2] == key:
            return separator2

        if key < arr[separator1]:
            return _ternary_search(arr, start, separator1-1, key)
        elif key < arr[separator2]:
            return _ternary_search(arr, separator1+1, separator2-1, key)
        else:
            return _ternary_search(arr, separator2+1, end, key)
    return None


if __name__ == '__main__':
    sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    key = 10
    index = ternary_search(sorted_arr, key)
    if index:
        print('{} found at index {}'.format(key, index))
    else:
        print('{} not found in the array'.format(key))

