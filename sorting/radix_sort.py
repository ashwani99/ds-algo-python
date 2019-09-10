def radix_sort(arr):
    maxx = max(arr)
    place = 1
    while maxx:
        counting_sort(arr, place)
        place *= 10
        maxx /= 10
    
    return arr


def counting_sort(arr, place):
    bucket = []
    for _ in range(10):
        bucket.append([])

    for item in arr:
        bucket_key = (item//place)%10
        bucket[bucket_key].append(item)

    arr.clear()
    for item in bucket:
        arr.extend(item)


if __name__ == '__main__':
    print(radix_sort([3, 5, 55, 121, 0, 101, 10, 999, 996, 69]))
