def selection_sort(arr):
    l = len(arr)
    for index, item in enumerate(arr):
        mini_id = index
        for i in range(index+1, l):
            if arr[i] < arr[mini_id]:
                mini_id = i
        arr[index], arr[mini_id] = arr[mini_id], arr[index]
    return arr


if __name__ == '__main__':
    arr = [5, 4, 3, 2, 1, 0, -6]
    print(selection_sort(arr))
