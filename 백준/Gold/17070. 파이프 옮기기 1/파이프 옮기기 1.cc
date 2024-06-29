#include <iostream>
#include <vector>

using namespace std;

int countWaysToMovePipe(int N, vector<vector<int>>& house) {
    vector<vector<vector<int>>> dp(N+1, vector<vector<int>>(N+1, vector<int>(3, 0)));
    dp[1][2][0] = 1;

    for (int i = 1; i <= N; ++i) {
        for (int j = 1; j <= N; ++j) {
            if (house[i-1][j-1] == 1) continue;

            if (j > 1 && house[i-1][j-2] == 0) {
                dp[i][j][0] += dp[i][j-1][0] + dp[i][j-1][2];
            }
            if (i > 1 && house[i-2][j-1] == 0) {
                dp[i][j][1] += dp[i-1][j][1] + dp[i-1][j][2];
            }
            if (i > 1 && j > 1 && house[i-2][j-2] == 0 && house[i-2][j-1] == 0 && house[i-1][j-2] == 0) {
                dp[i][j][2] += dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2];
            }
        }
    }

    return dp[N][N][0] + dp[N][N][1] + dp[N][N][2];
}

int main() {
    int N;
    cin >> N;
    vector<vector<int>> house(N, vector<int>(N));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> house[i][j];
        }
    }

    cout << countWaysToMovePipe(N, house) << endl;
    return 0;
}