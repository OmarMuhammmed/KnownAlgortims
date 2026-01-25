def quick_sort(arr):
    
    if len(arr)<2:
        return arr
    
    else :
        pivot = arr[0]
        less = [i for i in arr[1:] if 1 <=pivot]
        greater = [i for i in arr[1:] if 1 >pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)
    
print(quick_sort([10, 3, 1, 6, 7, 0, 2]))    

