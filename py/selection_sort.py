
def find_min(arr, start, end ):
    min_index = start
    for i in range(start + 1, end):
        if arr[i] < arr[min_index]:
            min_index = i
    return min_index

def selection_sort(arr):
   for i in range(len(arr)):
       min_index = find_min(arr, i, len(arr))
       arr[i], arr[min_index] = arr[min_index], arr[i]



 
def print_array(arr):
    for val in arr:
        print(val, end=" ")
    print()

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    
    print("Original array: ", end="")
    print_array(arr)
    
    selection_sort(arr)
    
    print("Sorted array: ", end="")
    print_array(arr)

# one function selection_sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1): # last Elment is sorted by default 

        min_idx = i
    
        for j in range(i + 1, n):

            if arr[j] < arr[min_idx]:

                min_idx = j
        
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]    