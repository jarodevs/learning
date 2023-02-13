array = [10, 8, 6, 2]

# Faire monter l'element le plus grand en haut de pile


def bubble_sort(array):
    n = len(array)
    while n > 1:
        newn = 0
        for i in range(1, n):
            if array[i-1] > array[i]:
                array[i-1], array[i] = array[i], array[i-1]
                newn = i
        n = newn
        print(array)
    return array

# n is the max range we will loop through
# newn is the going to set the n at the end of the array loop
# newn is calculated everytime a swap happened, which means that at the end of each array loop, the biggest item should be at the end of the array and therefore sorted
# the bubble sort basically means that after each array item iteration, the biggest, non treated  item is sorted


print(bubble_sort(array))
