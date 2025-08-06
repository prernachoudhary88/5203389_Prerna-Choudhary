void miniMaxSum(int arr_count, int* arr) {
    long total = 0;
    int min = INT_MAX;
    int max = INT_MIN;
    
    for(int i = 0; i<arr_count; i++){
        total += arr[i];
        if(arr[i]<min) min = arr[i];
        if (arr[i]>max) max = arr[i];
    }
    long min_sum = total - max;
    long max_sum = total - min;
    
    printf("%ld %ld\n", min_sum, max_sum);

}
