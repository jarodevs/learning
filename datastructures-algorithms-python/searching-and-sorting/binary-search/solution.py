def binary_search(input_array, value):
    input_array = sorted(input_array)
    low = 0
    high = len(input_array) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if value == input_array[mid]:
            return mid
        elif value > input_array[mid]:
            low = mid + 1
        elif value < input_array[mid]:
            high = mid - 1
    return -1


def binary_search_recursive(low, high, input_array, value):
    if low <= high:
        mid = low + (high - low)//2
        if value == input_array[mid]:
            return mid
        elif value > input_array[mid]:
            return binary_search_recursive(mid+1, high, input_array, value)
        elif value < input_array[mid]:
            return binary_search_recursive(low, high-1, input_array, value)
    else:
        return -1


input = [1, 2, 3, 4, 5]
# print(binary_search(input, 9))
print(binary_search_recursive(0, len(input) - 1, input, 9))
