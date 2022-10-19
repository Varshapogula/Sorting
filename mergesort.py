def MergeSort(arr1):
    if len(arr1) > 1:  
        r = len(arr1)//2
        L = arr1[:r]
        M = arr1[r:]
        MergeSort(L)
        MergeSort(M)
        i = j = k = 0
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                arr1[k] = L[i]
                i += 1
            else:
                arr1[k] = M[j]
                j += 1
            k += 1
        while i < len(L):
            arr1[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            arr1[k] = M[j]
            j += 1
            k += 1
arr1 = [8,2,11,7,5,4]
MergeSort(arr1)
print("The Array After Sorted Is :  ",arr1)
