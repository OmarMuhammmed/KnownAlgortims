#include <iostream>
#include <bits/stdc++.h>
using namespace std;


int findMin(int arr[], int size, int start) {
    int minIndex = start;
    for(int i = start + 1; i < size; i++) {
        if(arr[i] < arr[minIndex]) {
            minIndex = i;
        }
    }
    return minIndex;
}

void Swap(int &x, int &y)
{
    int temp = x ;
    x = y ; 
    y = temp ; 
}

void selectionSort(int arr[], int size)
{
    for (int i = 0 ; i< size-1 ; i++)
    {
        int min = findMin(arr, size , i);
        Swap(arr[i], arr[min]);
    }
}

void printArray(int arr[], int size) {
    for(int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
   
}
 

int main() {
    int arr[]= {22,33,44,66,77,99,11};
    int size = sizeof(arr) / sizeof(arr[0]); 

    cout << "Original array: ";
    printArray(arr, size);

    selectionSort(arr,size);
    cout <<endl ; 

    cout << "Sorted array: ";
    printArray(arr, size);

    return 0;
}

// one function 
void selectionSort(vector<int> &arr) {
    int n = arr.size();

    for (int i = 0; i < n - 1; ++i) {
        int min_idx = i;

        for (int j = i + 1; j < n; ++j) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j; 
            }
        }
        
        swap(arr[i], arr[min_idx]);
    }
}