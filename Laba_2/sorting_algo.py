# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
# from typing import List


class Sort:

    @staticmethod
    def partition(array: list, low: int, high: int) -> int:
        i = (low - 1)  # index of smaller element
        pivot = array[high]  # pivot

        for j in range(low, high):
            # If current element is smaller than or
            # equal to pivot
            if array[j] <= pivot:
                # increment index of smaller element
                i = i + 1
                array[i], array[j] = array[j], array[i]

        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    # The main function that implements QuickSort
    # arr[] --> Array to be sorted,
    # low  --> Starting index,
    # high  --> Ending index

    # Function to do Quick sort

    @staticmethod
    def quick_sort(array: list, low: int, high: int) -> list:
        if len(array) == 1:
            return array
        if low < high:
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = Sort.partition(array, low, high)

            # Separately sort elements before
            # partition and after partition
            Sort.quick_sort(array, low, pi - 1)
            Sort.quick_sort(array, pi + 1, high)
        # return array

    @staticmethod
    def insertion_sort(array):
        # print(array)
        for i in range(1, len(array)):
            # Set key:
            key = array[i]

            j = i - 1
            while j >= 0 and array[j] > key:
                # Swap:
                array[j + 1] = array[j]
                array[j] = key

                # Decrement 'j':
                j -= 1
        # return array


if __name__ == '__main__':
    # Driver code to test above
    arr = [10, 7, 8, 5, 9, 1, 5, 5]
    print(arr)
    Sort.quick_sort(arr, 0, len(arr) - 1)
    print(arr)

    # print("Sorted array is:")
    # for i in range(n):
    #     print("%d" % arr[i])

