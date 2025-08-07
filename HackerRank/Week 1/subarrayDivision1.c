int birthday(int s_count, int* s, int d, int m) {
    int count = 0;
    
    for (int i = 0; i <= s_count - m; i++) {
        int current_sum = 0;
        
        for (int j = 0; j < m; j++) {
            current_sum += s[i + j];
        }
        
        if (current_sum == d) {
            count++;
        }
    }
    
    return count;
}
