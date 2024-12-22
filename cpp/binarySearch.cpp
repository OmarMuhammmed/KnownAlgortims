#include <iostream>
using namespace std;


int binarySearch(int arr[], int size, int value)
{
    int low = 0 ;
    int high = size - 1 ;

    while ( low <= high ) 
    {
        int mid = (low + high) / 2 ; 
        if (arr[mid] == value) 
            return mid ; 

        else if (arr[mid] < value)  
            low = mid + 1 ;

        else 
            high = mid - 1 ;  
    }
    return -1 ; 
}






int main()
{
    int arr[] = { 2, 3, 4, 10, 40 };
    int size = sizeof(arr)/sizeof(arr[0]);
    int result = binarySearch(arr, size, 10) ;
    if(result == -1) cout << "Element is not present in array";
    else cout << "Element is present at index " << result;
    return 0;
}