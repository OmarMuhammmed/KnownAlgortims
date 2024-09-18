def selection_sort(arr):
    """
    The `selection_sort` function implements the selection sort algorithm to sort a given array in
    ascending order.
    
    :param arr: The `selection_sort` function you provided implements the selection sort algorithm to
    sort a given list `arr` in ascending order. The function iterates through the list and selects the
    minimum element in each iteration and swaps it with the element at the current position
    :return: The `selection_sort` function is returning the input array `arr` after sorting it in
    ascending order using the selection sort algorithm.
    """
    n = len(arr)
    print(n)  
    # n = 3
    for j in range(n - 1):  
        # [6,9]
        iMin = j
        # imin = 6 
        #  
        for i in range(j + 1, n):  
            # i = 
            if arr[i] < arr[iMin]: 
                iMin = i  
        
        arr[j], arr[iMin] = arr[iMin], arr[j]
    return arr

# arr = [6,9,5]
# print(selection_sort(arr))


def selection_sort(arr):
    """
            Length of array: 3
            Outer loop iteration 0:
            Array at the start: [3, 1, 2]
            iMin initialized to index 0, value = 3
            Checking if arr[1] < arr[0]
            Comparing: 1 < 3
            Found new iMin at index 1, value = 1
            Checking if arr[2] < arr[1]
            Comparing: 2 < 1
            Swapping arr[0] = 3 with arr[1] = 1
            Array after swap: [1, 3, 2]
            Outer loop iteration 1:
            Array at the start: [1, 3, 2]
            iMin initialized to index 1, value = 3
            Checking if arr[2] < arr[1]
            Comparing: 2 < 3
            Found new iMin at index 2, value = 2
            Swapping arr[1] = 3 with arr[2] = 2
            Array after swap: [1, 2, 3]
            Sorted array: [1, 2, 3]
            """
    n = len(arr)
    print(f"Length of array: {n}")  # طول المصفوفة = 3
    for j in range(n - 1):  
        # الحلقة الخارجية بتعدّ من 0 لـ n-2
        print(f"\nOuter loop iteration {j}:")
        print(f"Array at the start: {arr}")
        iMin = j
        # iMin هيكون في البداية = j (أول عنصر غير مرتب)
        print(f"iMin initialized to index {iMin}, value = {arr[iMin]}")
        
        for i in range(j + 1, n):  
            # الحلقة الداخلية بتدور على أقل عنصر في الجزء الغير مرتب
            print(f"  Checking if arr[{i}] < arr[{iMin}]")
            print(f"  Comparing: {arr[i]} < {arr[iMin]}")
            if arr[i] < arr[iMin]: 
                iMin = i  
                print(f"  Found new iMin at index {iMin}, value = {arr[iMin]}")
        
        # تبديل (swap) بين arr[j] و arr[iMin]
        print(f"Swapping arr[{j}] = {arr[j]} with arr[{iMin}] = {arr[iMin]}")
        arr[j], arr[iMin] = arr[iMin], arr[j]
        print(f"Array after swap: {arr}")
    
    return arr

arr = [3, 1, 2]
sorted_arr = selection_sort(arr)
print(f"\nSorted array: {sorted_arr}")