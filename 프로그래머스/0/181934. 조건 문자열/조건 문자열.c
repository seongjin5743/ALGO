#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(const char* ineq, const char* eq, int n, int m) {
    int answer = 0;

    if (ineq[0] == '>') {
        if (eq[0] == '=') {
            answer = (n >= m);
        } else { // eq == "!"
            answer = (n > m);
        }
    } else if (ineq[0] == '<') {
        if (eq[0] == '=') {
            answer = (n <= m);
        } else { // eq == "!"
            answer = (n < m);
        }
    }

    return answer;
}
