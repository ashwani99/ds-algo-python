def insertion_sort(arr):
    for i in range(len(arr)):
        temp = arr[i]
        mover = i
        while mover > 0 and arr[mover-1] > temp:
            arr[mover] = arr[mover-1]
            mover -= 1
        arr[mover] = temp
        print('After pass {}: {}'.format(i+1, arr))


if __name__ == '__main__':
    insertion_sort([5, 4, 6, 7 ,8, 2, 1, -80])
