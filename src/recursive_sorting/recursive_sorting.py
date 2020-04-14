# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    nA = len( arrA )
    nB = len( arrB )
    i = 0
    j = 0
    k = 0
    while i < nA and j < nB:
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1
        else:
            merged_arr[k] = arrB[j]
            j += 1
        k += 1
    while i < nA:
        merged_arr[k] = arrA[i]
        i += 1
        k += 1
    while j < nB:
        merged_arr[k] = arrB[j]
        j += 1
        k += 1  
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    n = len(arr)
    mid = n // 2
    sorted_arr = []
    if n > 1:
        a = arr[mid:]
        b = arr[:mid]

        a = merge_sort(a)
        b = merge_sort(b)
        arr = merge(a,b)
    print(arr)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
