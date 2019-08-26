def bubble_sort(arr):
    l = len(arr)
    for i in range(l-1):
        swaps = 0
        for j in range(l-i-1):
            if arr[j] > arr[j+1]:
                swaps += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
        # modified bubble sort
        # if no swaps on this pass then array is sorted
        if swaps == 0:
            break
        print('After pass {}: {}'.format(i+1, arr))
    return arr


if __name__ == '__main__':
    arr = [9,7,6,5,4,3,-90, -0]
    print(bubble_sort(arr))
    print(bubble_sort([1, 2, 3, 4, -9]))
