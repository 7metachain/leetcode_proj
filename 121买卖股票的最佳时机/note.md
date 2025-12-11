# 笔记：买卖股票的最佳时机（单次交易）

> 结合原始笔记的全部要点，补全栈 / 动态规划 / 分治三种解法，附可运行的 Python 与 C++ 代码。

## 1. 问题简介
- 给定数组 `prices`，`prices[i]` 是第 `i` 天股价。
- 只能买入一次并在之后某天卖出一次，求最大利润；买入前必须卖出，若无利润返回 0。
- 输入：数组 `prices`；输出：最大利润。

## 2. 背后的自然思维
- 自然的直觉：

    几何视角：这个问题最直观的理解是把每一天的股票价格视为曲线，然后寻找最低点和最高点之间的差距，差值即为最大利润。

    转化为数组问题：由于计算机无法像我们画图一样直观地分析这条曲线，我们将价格看作一个离散的数组，然后通过遍历数组来模拟曲线的最小点和最大点之间的差距。

- 问题的抽象化：

    这个问题本质上是一个动态的变化问题，要求通过一系列的操作来更新状态，从而找出最优解。

    将这个问题映射到数组操作上，我们需要维护最小价格和最大利润这两个状态，以便逐步更新并最终获得最大利润。

## 3. 常规解法：一次遍历（O(n), O(1)）
- 思路：遍历时实时更新最低价和最大利润。
- 公式：`min_price = min(min_price, price)`；`max_profit = max(max_profit, price - min_price)`。
- 复杂度：时间 O(n)，空间 O(1)。

### 代码（Python，可运行）
```python
from typing import List


def max_profit(prices: List[int]) -> int:
    min_price = float("inf")
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


def main() -> None:
    import sys

    data = sys.stdin.read().strip().split()
    prices = list(map(int, data)) if data else []
    print(max_profit(prices))


if __name__ == "__main__":
    main()
```

### 代码（C++17，可运行）
```cpp
#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>

int maxProfit(const std::vector<int>& prices) {
    int min_price = INT_MAX;
    int max_profit = 0;
    for (int p : prices) {
        min_price = std::min(min_price, p);
        max_profit = std::max(max_profit, p - min_price);
    }
    return max_profit;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::vector<int> prices;
    int x;
    while (std::cin >> x) prices.push_back(x);
    std::cout << maxProfit(prices) << '\n';
    return 0;
}
```

运行示例：
- Python：`python3 /Users/jchen/Documents/leetcode_proj/121买卖股票的最佳时机/max_profit.py <<< "7 1 5 3 6 4"`
- C++：`g++ -std=c++17 /Users/jchen/Documents/leetcode_proj/121买卖股票的最佳时机/max_profit.cpp -o /Users/jchen/Documents/leetcode_proj/121买卖股票的最佳时机/max_profit && echo "7 1 5 3 6 4" | /Users/jchen/Documents/leetcode_proj/121买卖股票的最佳时机/max_profit`

## 4. 手动模拟示例（prices = [7, 1, 5, 3, 6, 4]）
- 初始化：`min_price = inf`，`max_profit = 0`
- 逐步：
  1) price=7 → min=7, profit=0  
  2) price=1 → min=1, profit=0  
  3) price=5 → min=1, profit=4  
  4) price=3 → min=1, profit=4  
  5) price=6 → min=1, profit=5  
  6) price=4 → min=1, profit=5  
- 最终最大利润 = 5。

## 5. 抽象化与数据结构映射
- 从自然思维到计算机实现：尽管问题本身可以通过曲线的最小点和最大点来直观理解，但计算机实现要求我们将其转化为离散的数组操作。我们不能直接使用几何曲线来求解，而是使用数组来模拟价格随时间的变化。

- 数据结构的使用：我们用数组表示股票的价格，利用最小值和最大利润的更新来模拟“曲线”上的最小点和最大点。

- 代码题的局限性：通过这种抽象化的方式，我们虽然失去了直观的几何感，但却能够在有限的时间和空间内高效地解决问题。

## 6. 其他三种解法与代码

### 6.1 栈（单调递增段）
- 思路：用递增栈维护一段上涨区间，遇到下降或结束时结算该区间的最高-最低差。
- 复杂度：O(n) 时间，O(n) 空间。

```python
def max_profit_stack(prices):
    if not prices:
        return 0
    stack = []
    ans = 0
    for p in prices + [float("inf")]:  # 哨兵触发最后结算
        while stack and p < stack[-1]:
            high = stack[-1]
            low = stack[0]
            ans = max(ans, high - low)
            stack.pop()
        stack.append(p)
    return ans
```

```cpp
int maxProfitStack(const std::vector<int>& prices) {
    if (prices.empty()) return 0;
    std::vector<int> st;
    int ans = 0;
    for (int idx = 0; idx <= (int)prices.size(); ++idx) {
        int p = (idx == (int)prices.size()) ? INT_MAX : prices[idx];
        while (!st.empty() && p < st.back()) {
            int high = st.back();
            int low = st.front();
            ans = std::max(ans, high - low);
            st.pop_back();
        }
        st.push_back(p);
    }
    return ans;
}
```

### 6.2 动态规划（状态机写法）
- 状态：
  - `hold`：持有一股后的最大现金（允许买一次），初始 `-prices[0]`
  - `sold`：未持有的最大现金，初始 0
- 转移：`hold = max(hold, -prices[i])`；`sold = max(sold, hold + prices[i])`
- 复杂度：O(n) 时间，O(1) 空间。

```python
def max_profit_dp_state(prices):
    if not prices:
        return 0
    hold = -prices[0]
    sold = 0
    for p in prices[1:]:
        hold = max(hold, -p)
        sold = max(sold, hold + p)
    return sold
```

```cpp
int maxProfitDPState(const std::vector<int>& prices) {
    if (prices.empty()) return 0;
    int hold = -prices[0];
    int sold = 0;
    for (size_t i = 1; i < prices.size(); ++i) {
        hold = std::max(hold, -prices[i]);
        sold = std::max(sold, hold + prices[i]);
    }
    return sold;
}
```

### 6.3 分治（最大子段和变形）
- 思想：利润 = `prices[j] - prices[i] (j>i)`；定义差分 `diff[k] = prices[k+1] - prices[k]`，求 `diff` 的最大子段和。
- 分治：求左、右、跨中三段最大值，取最大。
- 复杂度：O(n log n) 时间，O(log n) 递归栈。

```python
def max_profit_divide(prices):
    if len(prices) < 2:
        return 0
    diff = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]

    def solve(l, r):
        if l == r:
            return max(diff[l], 0)
        m = (l + r) // 2
        left = solve(l, m)
        right = solve(m + 1, r)
        best_left = cur = 0
        for i in range(m, l - 1, -1):
            cur += diff[i]
            best_left = max(best_left, cur)
        best_right = cur = 0
        for i in range(m + 1, r + 1):
            cur += diff[i]
            best_right = max(best_right, cur)
        cross = best_left + best_right
        return max(left, right, cross)

    return solve(0, len(diff) - 1)
```

```cpp
int maxProfitDivide(const std::vector<int>& prices) {
    if (prices.size() < 2) return 0;
    std::vector<int> diff(prices.size() - 1);
    for (size_t i = 0; i + 1 < prices.size(); ++i) diff[i] = prices[i + 1] - prices[i];
    std::function<int(int, int)> solve = [&](int l, int r) -> int {
        if (l == r) return std::max(diff[l], 0);
        int m = (l + r) / 2;
        int left = solve(l, m);
        int right = solve(m + 1, r);
        int best_left = 0, cur = 0;
        for (int i = m; i >= l; --i) {
            cur += diff[i];
            best_left = std::max(best_left, cur);
        }
        int best_right = 0;
        cur = 0;
        for (int i = m + 1; i <= r; ++i) {
            cur += diff[i];
            best_right = std::max(best_right, cur);
        }
        int cross = best_left + best_right;
        return std::max({left, right, cross});
    };
    return solve(0, (int)diff.size() - 1);
}
```

## 7. 自然思维与抽象
- 直观：最低点到最高点的差距。
- 抽象：转成数组与状态更新；失去几何直观，但得到线性时间、常数空间。

## 8. 其他方法尝试（概念）
- 栈：维护递增段，遇降结算涨幅。
- 动态规划：状态机两变量，等价于一次遍历。
- 分治：差分数组的最大子段和。

## 9. 总结与反思
- 工程上最推荐：一次遍历（O(n), O(1)），简单高效。
- 其他方法可作为思路拓展；性能或实现复杂度上不如一次遍历，但有助于理解问题的不同角度。

