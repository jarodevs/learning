def merge_sort(list):
    arr_len = len(list)

    if arr_len == 1:
        return list

    mid = arr_len // 2

    larray = merge_sort(list[:mid])
    rarray = merge_sort(list[mid:])

    return merge(larray, rarray)


def merge(larray, rarray):
    output = []
    i = j = 0
    larray_length = len(larray)
    rarray_length = len(rarray)

    while i < larray_length and j < rarray_length:
        larray_current = larray[i]
        rarray_current = rarray[j]

        if larray_current < rarray_current:
            output.append(larray_current)
            i += 1
        else:
            output.append(rarray_current)
            j += 1
    if i < larray_length:
        output.extend(larray[i:])
    if j < rarray_length:
        output.extend(rarray[j:])

    return output


print(merge_sort([6, 2, 7, 2, 4, 1, 7, 3, 2, 12, 654, 23]))
