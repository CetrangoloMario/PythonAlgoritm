def pivot(array, start, end):
    # initializing
    pivot = array[start]
    low = start + 1
    high = end

    while True:

        # moving high towards left
        while low <= high and array[high] >= pivot:
            high = high - 1

        # moving low towards right
        while low <= high and array[low] <= pivot:
            low = low + 1
# checking if low and high have crossed
        if low <= high:

    # swapping values to rearrange
            array[low], array[high] = array[high], array[low]

        else:
    # breaking out of the loop if low > high
            break

# swapping pivot with high so that pivot is at its right # #position
        array[start], array[high] = array[high], array[start]

# returning pivot position
    return high


def quickSort(array, start, end):
    if start >= end:
        return

    # call pivot
    p = pivot(array, start, end)
    # recursive call on left half
    quickSort(array, start, p- 1)
    # recursive call on right half
    quickSort(array, p + 1, end)