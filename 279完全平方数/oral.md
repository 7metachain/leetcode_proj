## 279. 完全平方数（口播稿）

### 中文口播（推荐解法：动态规划）
这题给一个整数 `n`，要把 `n` 表示成若干个完全平方数（1、4、9、16…）之和，问**最少需要几个**。  
常见直觉是贪心“每次拿最大的平方数”，但它不保证最优，比如 12 贪心是 9+1+1+1=4，而最优是 4+4+4=3。  
稳妥解法是动态规划：先预处理所有 `<= n` 的平方数 `squares`。定义 `dp[i]` 表示凑成和为 `i` 的最少平方数个数。初始化 `dp[0]=0`，其余为无穷大。  
转移就是枚举最后一个平方数 `sq`：  
`dp[i] = min(dp[i], dp[i - sq] + 1)`（前提是 `sq <= i`）。  
这样从 `1..n` 递推，最终 `dp[n]` 就是答案。  
复杂度：平方数个数约是 `sqrt(n)`，所以时间 O(n·sqrt(n))，空间 O(n)，在 `n<=10^4` 下完全可行。

### English (Recommended: DP)
Given an integer `n`, we want the minimum number of perfect squares (1, 4, 9, 16, …) whose sum equals `n`.  
A greedy strategy like “take the largest square first” is not always optimal—for example, `12` becomes `9+1+1+1` (4 squares) but the optimum is `4+4+4` (3 squares).  
The robust approach is dynamic programming. Precompute all squares `<= n`. Let `dp[i]` be the minimum number of squares to sum to `i`. Initialize `dp[0]=0` and others to infinity.  
Transition: for each `i` and each square `sq <= i`,  
`dp[i] = min(dp[i], dp[i - sq] + 1)`.  
Compute `dp` from 1 up to `n`; the answer is `dp[n]`.  
There are about `sqrt(n)` squares, so time is O(n·sqrt(n)) and space is O(n), which is fine for `n <= 10^4`.


