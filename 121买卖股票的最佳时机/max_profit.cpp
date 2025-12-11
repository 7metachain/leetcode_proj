#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>

int maxProfit(const std::vector<int>& prices) {
    int min_price = INT_MAX;
    int max_profit = 0;
    for (int p : prices) {
        if (p < min_price) {
            min_price = p;
        } else {
            max_profit = std::max(max_profit, p - min_price);
        }
    }
    return max_profit;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::vector<int> prices;
    int x;
    while (std::cin >> x) {
        prices.push_back(x);
    }
    std::cout << maxProfit(prices) << '\n';
    return 0;
}

