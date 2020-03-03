# Sorting_Algorithms_Implementations
## 6 Common Sorting Algorithms In File
### Bubble,Insertion,Selection,Merge,Quick,Heap

```
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```
