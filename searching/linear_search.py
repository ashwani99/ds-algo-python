def search(arr, key):
    for index, item in enumerate(arr):
        if item == key:
            return index
    return None


if __name__ == '__main__':
    arr = [1,2,3,4,5,56,0, -1, -345]
    key = 99
    index = search(arr, key)
    if index:
        print('{} found at index: {}'.format(key, index))
    else:
        print('{} not found in the array'.format(key))
