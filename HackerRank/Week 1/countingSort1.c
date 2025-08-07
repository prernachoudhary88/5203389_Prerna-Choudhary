int* countingSort(int arr_count, int* arr, int* result_count) {
    
    *result_count = 100;
    
    int* frequency_array = (int*)calloc(100, sizeof(int));
    if (frequency_array == NULL) {
        return NULL;
    }
    
    for (int i = 0; i < arr_count; i++) {
        if (arr[i] >= 0 && arr[i] < 100) {
            frequency_array[arr[i]]++;
        }
    }
    
    return frequency_array;
}
