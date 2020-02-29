def quick_sort(sequence):
    length_sequesnce=len(sequence)
    if length_sequesnce <= 1:
        return sequence
    else:
        middle=sequence.pop()
        
    little_front=[]
    little_back=[]
    
    for item in sequence:
        if item >middle:
            little_back.append(item)
        else:
            little_front.append(item)
    return  quick_sort(little_back) + [middle] + quick_sort(little_front)       
        
        
print(quick_sort([1,3,6,1,2,4,6,2,5,4,8,4,5,6,4,8,7,6,2,3,5,7,9,5,4,3,2,1,3,2,1,3,2,1,5,4,6,3,2,1,4,5,6,3,9,1,2,3]))    
    
