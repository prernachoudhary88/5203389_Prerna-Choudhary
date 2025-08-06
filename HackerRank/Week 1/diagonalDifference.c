int diagonalDifference(int arr_rows, int arr_columns, int** arr) {
    int leftToRightSum = 0;
    int rightToLeftSum = 0;
    
    for (int i = 0; i < arr_rows; i++) {
        leftToRightSum += arr[i][i];
    }
    
    for (int i = 0; i < arr_rows; i++) {
        rightToLeftSum += arr[i][arr_rows - 1 - i];
    }
    
    int difference = leftToRightSum - rightToLeftSum;
    return abs(difference);
}
