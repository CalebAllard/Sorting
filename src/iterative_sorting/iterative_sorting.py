# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for n in range(i + 1, len(arr)):
            if arr[n] < arr[smallest_index]:
                smallest_index = n

        # TO-DO: swap
        if smallest_index != i:
            temp = arr[smallest_index]
            arr[smallest_index] = arr[i]
            arr[i] = temp



    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range( 1, len(arr)):
        for n in range(0, len(arr) - 1 ):
             if arr[n] > arr[n + 1]:
                temp = arr[n]
                arr[n] = arr[n + 1]
                arr[n + 1] = temp
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr