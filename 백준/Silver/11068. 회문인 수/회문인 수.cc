#include <iostream>
#include <string>

using namespace std;

bool isPalindrome(string s) {
    for (int i = 0; i < s.length() / 2; i++) {
        if (s[i] != s[s.length() - 1 - i]) {
            return false;
        }
    }
    return true;
}

string decimalToBase(int decimal, int base) {
    if (decimal == 0) {
        return "0";
    }

    string result = "";
    while (decimal > 0) {
        int remainder = decimal % base;
        char digit;
        if (remainder < 10) {
            digit = '0' + remainder;
        } else {
            digit = 'A' + (remainder - 10);
        }
        result = digit + result;
        decimal /= base;
    }

    return result;
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int r;
        cin >> r;
        bool found = false;
        for (int j = 2; j <= 64; j++) {
            int n = r;
            string s= decimalToBase(n, j);
            if (isPalindrome(s)) {
                cout << "1" << endl;
                found = true;
                break;
            }
        }
        if (!found) {
            cout << "0" << endl;
        }
    }

    return 0;
}