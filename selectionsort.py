def SelectionSort(list1):
    for i in range(len(list1)):
        least = i
        for k in range(i+1, len(list1)):
            if(list1[k] < list1[least]):
                least = k
        swap(list1,least,i)


def swap(list1,x,y):
    temp=list1[x]
    list1[x]=list1[y]
    list1[y]=temp

list1=[29,72,98,13,87,66,52,51,36]
print("The List Before Sorting Is : ",list1)
SelectionSort(list1)
print("The List After Sorting Is : ",list1)
    