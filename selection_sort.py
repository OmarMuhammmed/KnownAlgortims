def selection_sort(list):
    """
    The `selection_sort` function implements the selection sort algorithm to sort a given array in
    ascending order.
    
    :param arr: The `selection_sort` function you provided implements the selection sort algorithm to
    sort a given list `arr` in ascending order. The function iterates through the list and selects the
    minimum element in each iteration and swaps it with the element at the current position
    :return: The `selection_sort` function is returning the input array `arr` after sorting it in
    ascending order using the selection sort algorithm.
    """
    n = len(list)
   
    for j in range(n): 

        min_num = j
     
        for i in range(j + 1, n):  
            if list[i] < list[min_num]: 
                min_num = i  
        
        list[j], list[min_num] = list[min_num], list[j]
        
    return list

