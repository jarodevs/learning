# An example of merge sort.
# First, divide the list into the smallest unit(1 element)
# then compare each element with the adjacent list to sort and merge the two adjacent lists.
# Finally, all the elements are sorted and merged.

input_array = [4, 6, 2, 5, 3, 9, 0, 1]


def merge_sort(input_array):
    index = 1
    merge = []
    while index < len(input_array):
        if input_array[index] > input_array[index - 1]:
            merge.append([input_array[index-1], input_array[index]])
        else:
            merge.append([input_array[index], input_array[index-1]])
        index += 1


print(merge_sort(input_array))
