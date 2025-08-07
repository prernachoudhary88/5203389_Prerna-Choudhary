#include <stdio.h>
#include <string.h>

int main() {
    char s[101], t[101]; 
    scanf("%s", s);
    scanf("%s", t);

    char res[101];        
    int len = strlen(s);

    for (int i = 0; i < len; i++) {
        if (s[i] == t[i])
            res[i] = '0';
        else
            res[i] = '1';
    }
    res[len] = '\0';  

    printf("%s", res);  

    return 0;
}
