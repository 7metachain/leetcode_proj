# 560. 和为 K 的子数组 —— 学习笔记

---

## 题目

- **输入**：整数数组 `nums`，整数 `k`
- **输出**：数组中和为 `k` 的**连续非空子数组**的个数

---

## 一、你一开始的直觉：是不是必须整体遍历？

- 数组没有排序，元素可正可负；
- 因为没有单调性，不能靠"排序/双指针/滑窗"跳过区间；
- 所以如果按"枚举所有子数组"的方式，确实要遍历很多情况（O(n²)）。

**但关键是：**
> 我们不必枚举所有 `(l, r)` 对，而是用数学等价变形，把"找所有子数组"变成"扫一遍数组时统计数量"。

---

## 二、解法 1：暴力枚举（两层循环，能做但慢）

### 1）核心想法

枚举所有子数组的左右端点 `(l, r)`：
- `l` 从 `0` 到 `n-1`
- `r` 从 `l` 到 `n-1`
- 计算 `nums[l..r]` 的和，如果等于 `k`，答案加 1

### 2）复杂度

- 子数组总数：n(n+1)/2 ≈ O(n²)
- 每个子数组求和如果再遍历一次是 O(n)，那就变成 O(n³)（更不行）
- **常见优化**：在固定 `l` 时用累加维护当前和，让求和变成 O(1)，整体 O(n²)

### 3）C++ 代码（O(n²) 版本）

```cpp
int ans = 0;
for (int l = 0; l < n; l++) {
    long long sum = 0;
    for (int r = l; r < n; r++) {
        sum += nums[r];
        if (sum == k) ans++;
    }
}
return ans;
```

### 4）为什么会超时

`n` 最大 20000，n² = 4e8 级别，容易超时。

---

## 三、解法 2：前缀和 + 哈希表（一次遍历，O(n)）

### 1）第一步：前缀和定义（Prefix Sum）

**定义：**
```
pre[i] = nums[0] + nums[1] + ... + nums[i]
```

那么连续子数组 `[l..r]` 的和可以写成：
- 若 `l == 0`：`sum(0..r) = pre[r]`
- 若 `l > 0`：`sum(l..r) = pre[r] - pre[l-1]`

**这一步的意义：**
> 子数组求和可以用两个前缀和相减得到（O(1)）。

---

### 2）第二步：把"和为 k"改写成"前缀和差为 k"

**目标**：`sum(l..r) = k`

对于 `l > 0`：
```
pre[r] - pre[l-1] = k
```

移项得到：
```
pre[l-1] = pre[r] - k
```

**关键解释（这句要记牢）：**
> 当右端点固定为 `r` 时，所有满足条件的子数组个数 = 在 `r` 之前出现过多少次前缀和等于 `pre[r] - k`。

因为每出现一次 `pre[l-1] = pre[r] - k`，就对应一个子数组 `[l..r]` 的和为 `k`。

---

### 3）第三步：用哈希表记录"前缀和出现次数"

用 `cnt` 存储：
```
cnt[s] = 前缀和 s 出现的次数
```

扫描数组时维护当前前缀和 `sum`：
1. `sum += nums[i]`
2. 需要的历史前缀和是 `sum - k`，所以答案增加：`ans += cnt[sum - k]`
3. 再记录当前前缀和：`cnt[sum] += 1`

---

### 4）最容易漏的关键细节：为什么 `cnt[0] = 1`？

**初始化：**
> `cnt[0] = 1` 表示"空前缀（在任何元素之前）前缀和为 0 出现 1 次"

**作用：**
处理从下标 0 开始的子数组。

当某一刻 `sum == k` 时：
- `sum - k == 0`
- `cnt[0]` 会贡献 1
- 代表子数组 `[0..i]` 是一个合法解

**如果不设 `cnt[0] = 1`，所有从 0 开始的解都会漏掉。**

---

### 5）复杂度

- 每个元素只处理一次：时间 O(n)
- 哈希表最多存 n 种不同前缀和：空间 O(n)

---

### 6）完整代码（C++）

```cpp
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<long long, int> cnt;
        long long sum = 0;
        int ans = 0;

        cnt[0] = 1;  // 空前缀：前缀和为0先出现1次

        for (int x : nums) {
            sum += x;
            if (cnt.count(sum - k)) ans += cnt[sum - k];
            cnt[sum]++;
        }
        return ans;
    }
};
```

---

### 7）完整代码（Python3）

```python
from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1  # 空前缀

        s = 0
        ans = 0
        for x in nums:
            s += x
            ans += cnt[s - k]  # 统计之前出现过多少次 s-k
            cnt[s] += 1
        return ans
```

---

## 四、为什么"滑动窗口/双指针"不适合这题

滑动窗口需要"窗口扩大/缩小时，窗口和有单调性变化"才能不漏解。

但这题 `nums[i]` 可能为负数：
- 扩大窗口（右指针右移）可能让和变小
- 缩小窗口（左指针右移）可能让和变大

因此无法用"和大了就缩，和小了就扩"的规则保证正确性。

---

## 📦 本地运行

### 文件
- `subarray_sum.py`
- `subarray_sum.cpp`

### 输入格式（每组两行，直到 EOF 退出）
- 第 1 行：数组 `nums`（如 `[1,1,1]` 或 `1 1 1`）
- 第 2 行：整数 `k`

### 运行命令
```bash
# Python
python3 subarray_sum.py

# C++
g++ -std=c++17 subarray_sum.cpp -o subarray_sum && ./subarray_sum
```

### 示例
```
输入：
[1,1,1]
2

输出：2
```
