#include <climits>
#include <iostream>
#include <vector>

int numSquares(int n) {
    std::vector<int> squares;
    for (int i = 1; i * i <= n; ++i) {
        squares.push_back(i * i);
    }

    std::vector<int> dp(n + 1, INT_MAX);
    dp[0] = 0;

    for (int i = 1; i <= n; ++i) {
        for (int sq : squares) {
            if (sq > i) break;
            if (dp[i - sq] != INT_MAX) {
                dp[i] = std::min(dp[i], dp[i - sq] + 1);
            }
        }
    }

    return dp[n];
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    while (std::cin >> n) {
        std::cout << numSquares(n) << '\n';
    }
    return 0;
}

