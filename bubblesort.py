def BubbleSort(list1):
    for i in range(len(list1)-1,0,-1):
        for j in range(i):
            if list1[j]>list1[j+1]:
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp

list1 = [54,26,93,17,77,31,44,55,20]
print("The List Before Sorting:",list1)
BubbleSort(list1)
print("The List After Sorting:",list1)