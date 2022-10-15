def Insertion(list1):
    for i in range(1,len(list1)):
        temp=list1[i]
        k=i
        while(k>0 and temp <list1[k-1]):
            list1[k]=list1[k-1]
            k=k-1
            list1[k]=temp

list1=[17,26,54,77,93,31,44,55,20]
print("The List Before Sorting Is : ",list1)
print("The List After SOrting Is : ",Insertion(list1),list1)
