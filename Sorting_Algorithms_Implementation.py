import timeit
"""
Bubble Sort is an sorting algorithm going through the array if any two numbers are in descending orders, they are swapped. Therefore, the last element in the array for each loop
is sorted.
"""


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


"""
Selection Sort is an sorting algorithm that finds minimum element in the remaining array and placed it at the beginning of the unsorted part
"""


def selection_sort(arr):
    pointer = 0
    for i in range(len(arr)):
        min_index = arr.index(min(arr[i:len(arr)]))
        arr[pointer],arr[min_index] = arr[min_index],arr[pointer]
        pointer += 1
    return arr


"""
Insertion Sort is an sorting algorithm that picks up the current element and compare to every element in the sorted part, and insert into the correct position in the sorted part
"""


def insertion_sort(arr):
    last_index_sorted = 1
    for i in range (last_index_sorted,len(arr)):
        for j in range(last_index_sorted):
            if arr[i] < arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
        last_index_sorted += 1
    return arr


"""
Merge Sort is an sorting algorithm that keeps splitting into subarrays until length is 2 and then merge back together in a sorted order
"""

def merge_sort(arr):
    
    return arr

if __name__ == '__main__':
    sample = [4, 10, 5, 2, 99999, -1, 259, 94, 0, 91, 23, 6, 9900]
    print(insertion_sort(sample))

    print("you have located the treasure!")


