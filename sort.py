def insertion_sort(arr):
    """
    Sorts a list using the insertion sort algorithm

    :type arr: list
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j -1
        arr[j + 1] = key
