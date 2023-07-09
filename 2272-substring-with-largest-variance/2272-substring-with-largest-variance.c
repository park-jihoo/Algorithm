#include <stdbool.h>
#include <string.h>

#define MAX_CHARS 26

int kadane(char a, char b, const char* s) {
    int ans = 0;
    int countA = 0;
    int countB = 0;
    bool canExtendPrevB = false;

    for (int i = 0; s[i] != '\0'; ++i) {
        char c = s[i];
        if (c != a && c != b)
            continue;
        if (c == a)
            ++countA;
        else
            ++countB;
        if (countB > 0)
            ans = (countA - countB > ans) ? countA - countB : ans;
        else if (countB == 0 && canExtendPrevB)
            ans = (countA - 1 > ans) ? countA - 1 : ans;
        if (countB > countA) {
            countA = 0;
            countB = 0;
            canExtendPrevB = true;
        }
    }
    return ans;
}

int largestVariance(char* s) {
    bool unique_chars[MAX_CHARS] = { false };
    for (int i = 0; s[i] != '\0'; ++i)
        unique_chars[s[i] - 'a'] = true;
    int max_variance = 0;
    for (int i = 0; i < MAX_CHARS; ++i)
        for (int j = 0; j < MAX_CHARS; ++j)
            if (i != j && unique_chars[i] && unique_chars[j])
                max_variance = (kadane(i + 'a', j + 'a', s) > max_variance) ? kadane(i + 'a', j + 'a', s) : max_variance;
    return max_variance;
}