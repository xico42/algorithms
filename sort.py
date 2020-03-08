def insertion_sort(arr, reverse=False):
    """
    Sorts a list using the insertion sort algorithm

    :param reverse:  bool
    :type arr: list
    """

    def compare(first, second, reverse=False):
        if reverse:
            return first < second
        return first > second

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and compare(arr[j], key, reverse):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
