public class MergeSort {

    public static void mergeSort(int[] arr) {
        if (arr.length <= 1) return;

        int mid = arr.length / 2;
        int[] left = new int[mid];
        int[] right = new int[arr.length - mid];

        // Split array
        for (int i = 0; i < mid; i++) left[i] = arr[i];
        for (int i = mid; i < arr.length; i++) right[i - mid] = arr[i];

        // Recursively sort
        mergeSort(left);
        mergeSort(right);

        // Merge
        merge(arr, left, right);
    }

    private static void merge(int[] arr, int[] left, int[] right) {
        int i = 0, j = 0, k = 0;

        // Compare left & right
        while (i < left.length && j < right.length) {
            if (left[i] < right[j]) {
                arr[k++] = left[i++];
            } else {
                arr[k++] = right[j++];
            }
        }

        // Remaining elements
        while (i < left.length) arr[k++] = left[i++];
        while (j < right.length) arr[k++] = right[j++];
    }

    // Test
    public static void main(String[] args) {
        int[] arr = {8, 3, 2, 9};
        mergeSort(arr);

        for (int x : arr) System.out.print(x + " ");
    }
}
