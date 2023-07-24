class Solution {
public:
    double myPow(double x, int n) {
        double ans = 1.0;
        if (n == 0)
            return 1;
        if (n == INT_MIN){
            ++n;
            n *= -1;
            x = 1/x;
            return myPow(x*x, n/2);
        }

        if (n < 0){
            if (n == INT_MIN) ++ n;
            n *= -1;
            x = 1/x;
        }
        return myPow(x*x, n/2)*(n%2 ? x : 1);
    }
};