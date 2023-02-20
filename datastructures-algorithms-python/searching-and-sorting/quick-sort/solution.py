array = [43, 123, 6, 1, 3, 2, 7, 2, 12, 65, 321]


def quick_sort(array):

    lenArray = len(array)

    if lenArray <= 1:
        return array

    lower_than_pivot = []
    greater_than_pivot = []
    pivot = array.pop()

    for item in array:
        if item < pivot:
            lower_than_pivot.append(item)
        else:
            greater_than_pivot.append(item)

    return quick_sort(lower_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


print(quick_sort(array))
