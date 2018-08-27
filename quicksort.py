"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def quicksort(array):

    quicksorhelper(array,0,len(array)-1)
    return array

def quicksorhelper(array,first,last):

    if(first < last):
        pivot = getPivot(array,first,last)
        quicksorhelper(array,pivot+1,last)
        quicksorhelper(array,first,pivot-1)

def getPivot(array,first,last):


    pivot = array[first]
    i = 1
    j =last
    while i < j:
        while array[i] < pivot and i < j:
            i = i + 1
        while array[j] > pivot and i < j:
            j = j - 1
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
        #i = i + 1
        #j = j - 1

    temp = array[i-1]
    array[i-1] = pivot
    array[first] = temp

    return i


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)