# LeetCode 279：完全平方数（整理笔记）

## 题目要求
- 给定整数 `n`（1 ≤ n ≤ 10^4），求最少用几个完全平方数（1, 4, 9, 16...）之和表示 `n`。
- 示例：  
  - `n = 12` → `3`（4 + 4 + 4）  
  - `n = 13` → `2`（4 + 9）

## 解法一：动态规划（推荐）
- 定义：`dp[i]` 为凑出和为 `i` 所需的最少完全平方数个数。
- 转移：`dp[i] = min(dp[i], dp[i - sq] + 1)`，其中 `sq` 为所有 `sq <= i` 的平方数。
- 初始化：`dp[0] = 0`；其余位置为正无穷大。
- 计算顺序：`i` 从 1 增长到 `n`，平方数顺序从小到大。
- 复杂度：时间 O(n√n)，空间 O(n)。

### 参考代码（Python）
```python
class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        dp = [0] + [float("inf")] * n
        for i in range(1, n + 1):
            for sq in squares:
                if sq > i:
                    break
                dp[i] = min(dp[i], dp[i - sq] + 1)
        return dp[n]
```

### 参考代码（C++）
```cpp
class Solution {
public:
    int numSquares(int n) {
        vector<int> squares;
        for (int i = 1; i * i <= n; ++i) {
            squares.push_back(i * i);
        }

        vector<int> dp(n + 1, INT_MAX);
        dp[0] = 0;

        for (int i = 1; i <= n; ++i) {
            for (int sq : squares) {
                if (sq > i) break;
                if (dp[i - sq] != INT_MAX) {
                    dp[i] = min(dp[i], dp[i - sq] + 1);
                }
            }
        }
        return dp[n];
    }
};
```

## 关键逻辑拆解
- `dp[i]` 的含义：凑成和 `i` 的最少数量；初始值设为无穷大表示“尚未可达”。
- 遍历平方数时，把 `sq` 视为“最后加入的那个数”，前缀部分是 `i - sq`，因此方案数量是 `dp[i - sq] + 1`。
- 例：`n = 12`  
  - 1^2：`dp[11] + 1`  
  - 2^2：`dp[8] + 1 = 2 + 1 = 3`  
  - 3^2：`dp[3] + 1 = 3 + 1 = 4`  
  - 取最小值得到 3。

## 为什么贪心不对
- 直觉：每次取不超过 `n` 的最大平方数，直到减完。
- 反例：  
  - 12：贪心得 9 + 1 + 1 + 1 = 4（错），最优是 4 + 4 + 4 = 3。  
  - 18：贪心得 16 + 1 + 1 = 3（错），最优是 9 + 9 = 2。
- 贪心只能作启发，不能保证全局最优。

### 贪心示例代码（仅供对比，非正确解）
```python
import math

class Solution:
    def numSquares(self, n: int) -> int:
        count = 0
        while n > 0:
            x = int(math.isqrt(n))
            n -= x * x
            count += 1
        return count
```

```cpp
class Solution {
public:
    int numSquares(int n) {
        int count = 0;
        while (n > 0) {
            int x = (int)std::sqrt(n);
            n -= x * x;
            count++;
        }
        return count;
    }
};
```

## 方法对比
| 方法 | 正确性 | 思路 | 代码量 | 时间复杂度 |
| --- | --- | --- | --- | --- |
| 动态规划 | ✅ 正确 | 完全背包 | 中等 | O(n√n) |
| BFS（层数即答案） | ✅ 正确 | 最短路径 | 中等 | O(n√n) |
| 贪心 | ❌ 不保证 | 每次取最大平方 | 简单 | O(n) |