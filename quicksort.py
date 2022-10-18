def QuickSort(array1):
    Elements = len(array1)
    if Elements < 2:
        return array1
    CurrentPosition = 0 
    for i in range(1, Elements):
         if array1[i] <= array1[0]:
              CurrentPosition += 1
              temp = array1[i]
              array1[i] = array1[CurrentPosition]
              array1[CurrentPosition] = temp
    temp = array1[0]
    array1[0] = array1[CurrentPosition] 
    array1[CurrentPosition] = temp 
    left = QuickSort(array1[0:CurrentPosition]) 
    right = QuickSort(array1[CurrentPosition+1:Elements]) 
    array1 = left + [array1[CurrentPosition]] + right
    return array1
Array_to_be_sorted = [50,23,9,18,61,32]
print("The Original Elements In Array Are : ",Array_to_be_sorted)
print("The Elements In Sorted Array Are : ",QuickSort(Array_to_be_sorted))
