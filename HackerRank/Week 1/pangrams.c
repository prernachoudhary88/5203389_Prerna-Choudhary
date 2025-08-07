char* pangrams(char* s) {
    
    bool alphabet_present[26] = {false};
    int count = 0;

    for (int i = 0; s[i] != '\0'; i++) {
        char current_char = tolower(s[i]);
        if (current_char >= 'a' && current_char <= 'z') {
            int index = current_char - 'a';
            if (!alphabet_present[index]) {
                alphabet_present[index] = true;
                count++;
            }
        }
    }
    
    if (count == 26) {
        static char pangram_result[] = "pangram";
        return pangram_result;
    } else {
        static char not_pangram_result[] = "not pangram";
        return not_pangram_result;
    }
}
