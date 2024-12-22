
def binary_search(arr, value):

    high = len(arr) - 1 
    low = 0 

    while high >= low :
        mid = (high + low) // 2 

        if arr[mid] == value :
            return mid 
        
        elif arr[mid] < value :
            low = mid + 1 

        else :
            high = mid -1 

    return -1         


if __name__ == '__main__':
    arr = [2,3,5,6,9,13,21,77]
    index = binary_search(arr, 9)

    if index == -1 :
        print("not in array")
    else : 
        print(f"Element in Index {index}")    