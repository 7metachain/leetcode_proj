## 121. 买卖股票的最佳时机（口播稿）

### 中文口播（推荐解法：一次遍历）
这题给一个数组 `prices`，`prices[i]` 表示第 i 天价格。要求只能交易一次：先买后卖，问最大利润；如果赚不到钱就返回 0。  
我会用一个非常直观的“最低点-当前价”的思路：从左到右扫一遍，维护两个量：**到目前为止的最低买入价 `min_price`**，以及**当前最大利润 `max_profit`**。  
每来一个新价格 `p`，先更新 `min_price = min(min_price, p)`；然后利润候选就是 `p - min_price`，用它去更新 `max_profit`。  
为什么对？因为对于任意一天卖出，最优买入一定是它之前出现过的最低价；我们把“历史最低价”一直维护住，就等价于在所有合法买入日里取最优。  
时间复杂度 O(n)，空间 O(1)。常见坑是忘记“只能卖在买之后”，但这个写法天然保证；还有就是如果一直下降，`max_profit` 仍然保持 0。

### English (Recommended: one pass)
We’re given `prices`, where `prices[i]` is the stock price on day i. We can make **at most one transaction**: buy once, then sell later, and return the maximum profit (or 0 if no profit).  
The key idea is “sell today minus the best buy price so far.” I scan from left to right and maintain two variables: **`min_price`**, the lowest price seen so far, and **`max_profit`**, the best profit so far.  
For each price `p`, update `min_price = min(min_price, p)`, then update `max_profit = max(max_profit, p - min_price)`.  
This works because if we sell on day i, the best buy day must be the minimum price among days `< i`, and we keep that minimum as we go.  
Time is O(n) and extra space is O(1). If prices only go down, `max_profit` stays 0.


