#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* my_string, int n) {
    int length = strlen(my_string);
    if (n > length) {
        n = length;
    }
    char* answer = (char*)malloc(sizeof(char) * (n + 1));
    if (answer == NULL) {
        return NULL;
    }
    
    const char* start_ptr = my_string + (length - n);
    strncpy(answer, start_ptr, n);
    answer[n] = '\0';
    
    return answer;
}