
def linear_search(arr, N, key):
    for i in range(0, N):
        if (arr[i] == key):
            return i
    return -1



if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40, 33]
    key = 33
    N = len(arr)

    result = linear_search(arr, N, key)
    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)