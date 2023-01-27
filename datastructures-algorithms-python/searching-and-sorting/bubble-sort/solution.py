def bubble_sort(array):
    n = len(array)
    while n > 1:
        newn = 0
        for i in range(1, n):
            if array[i-1] > array[i]:
                array[i-1], array[i] = array[i], array[i-1]
                newn = i
        n = newn
    return array


array = [5, 4, 2, 1, 10, 4, 5]
print(bubble_sort(array))
