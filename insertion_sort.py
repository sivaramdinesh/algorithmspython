def insertion_sort(list_a):
    indexing_length=range(1,len(list_a))
    for i in indexing_length:
        value_sort=list_a[i]
        
        while list_a[i-1]>value_sort and i>0:
            list_a[i],list_a[i-1]=list_a[i-1],list_a[i]
            i=i-1
            
    return list_a
print(insertion_sort([1,3,6,1,2,4,6,2,5,4,8,4,5,6,4,8,7,6,2,3,5,7,9,5,4,3,2,1,3,2,1,3,2,1,5,4,6,3,2,1,4,5,6,3,9,1,2,3]))
