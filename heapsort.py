def HeapSort(arr, n, i):
   largest  = i 
   l = 2 * i + 1 
   r = 2 * i + 2 
   if l < n and arr[i] < arr[l]:
      largest = l
   if r < n and arr[largest] < arr[r]:
      largest = r   
   if largest != i:
      arr[i],arr[largest] = arr[largest],arr[i]     
      HeapSort(arr, n, largest)
def heap(arr):
   n = len(arr)  
   for i in range(n, -1, -1):
      HeapSort(arr, n, i)
   for i in range(n-1, 0, -1):
      arr[i], arr[0] = arr[0], arr[i] 
      HeapSort(arr, i, 0)
arr = [2,9,7,6,5,8]
heap(arr)
n = len(arr)
print ("The Array After Sorted Is : ")
for i in range(n):
   print (arr[i],end=" ")
