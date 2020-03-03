# Sorting_Algorithms_Implementations
## 6 Common Sorting Algorithms In File
### Bubble Sort
Bubble Sort is an sorting algorithm going through the array if any two numbers are in descending orders, they are swapped. Therefore, the last element in the array for each loop is sorted.
```
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```
### Selection Sort
Selection Sort is an sorting algorithm that finds minimum element in the remaining array and placed it at the beginning of the unsorted part
```
def selection_sort(arr):
    pointer = 0
    for i in range(len(arr)):
        min_index = arr.index(min(arr[i:len(arr)]))
        arr[pointer], arr[min_index] = arr[min_index], arr[pointer]
        pointer += 1
    return arr
```
### Insertion Sort
Insertion Sort is an sorting algorithm that picks up the current element and compare to every element in the sorted part, and insert into the correct position in the sorted part
```
def insertion_sort(arr):
    last_index_sorted = 1
    for i in range(last_index_sorted, len(arr)):
        for j in range(last_index_sorted):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        last_index_sorted += 1
    return arr
```
### Merge Sort
Merge Sort is an sorting algorithm that keeps splitting into subarrays until length is 1 and then merge back together in a sorted order
```
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_subarray = arr[:mid]
        right_subarray = arr[mid:]

        merge_sort(left_subarray)
        merge_sort(right_subarray)

        i = j = k = 0

        while i < len(left_subarray) and j < len(right_subarray):
            if left_subarray[i] > right_subarray[j]:
                arr[k] = right_subarray[j]
                j += 1
            else:
                arr[k] = left_subarray[i]
                i += 1
            k += 1

        while i < len(left_subarray):
            arr[k] = left_subarray[i]
            i += 1
            k += 1

        while j < len(right_subarray):
            arr[k] = right_subarray[j]
            j += 1
            k += 1
    return arr
```
### Quick Sort
Quick Sort is an sorting algorithm that selects an element (first,last,random,median) as the pivot each loop and put all elements smaller before it, all greater ones after it, so that pivot is in the right spot.
```
def partition(arr, low, high):
    i = low - 1
    for j in range(low, high):
        if arr[j] < arr[high]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)

        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    return arr
```
### Heap Sort
Heap Sort is an sorting algorithm that builds a heap tree from unsorted array and take the root out in each iteration, then the array is sorted
```
def heapify(arr, n, i):
    root = i
    left_node = 2 * i + 1
    right_node = 2 * i + 2

    if left_node < n and arr[left_node] > arr[root]:
        root = left_node

    if right_node < n and arr[right_node] > arr[root]:
        root = right_node

    if root != i:
        arr[root], arr[i] = arr[i], arr[root]
        heapify(arr, n, root)


def heap_sort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for j in range(n - 1, 0, -1):
        arr[j], arr[0] = arr[0], arr[j]
        heapify(arr, j, 0)

    return arr
```
