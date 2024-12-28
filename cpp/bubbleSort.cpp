#include <iostream>
using namespace std;

void bubbleSort(int arr[], int size) {
    // last i elements are already sorted becuse one iteration sorts one elements in the End
    for (int i = 0; i < size - 1; i++) 
    { 
        // Last i elements are already sorted, so we don't need to check them
        // because every iteration we sort one element in the end and i updated for 1 iteration 
        for (int j = 0; j < size - i - 1; j++) 
        { 
            if (arr[j] > arr[j + 1]) 
            { 
                Swap(arr[j], arr[j + 1]);
            }
        }
    }
}
void Swap(int &x, int &y)
{
    int temp = x ;
    x = y ; 
    y = temp ; 
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]); // Length of array 

    cout << "Original array: ";
    printArray(arr, n);

    bubbleSort(arr, n);

    cout << "Sorted array: ";
    printArray(arr, n);

    return 0;
}
