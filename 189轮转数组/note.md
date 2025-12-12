# 189. 轮转数组

## 题目
给定一个整数数组 `nums`，将数组中的元素向右轮转 `k` 个位置，其中 `k` 是非负数。

## 本地可运行版本（Python / C++）
本目录提供两份可直接运行的程序（默认使用“三次翻转”的原地 O(1) 解法）：
- `rotate_array.py`
- `rotate_array.cpp`

输入格式（可重复多组，直到 EOF 结束）：
- 第 1 行：数组 `nums`（支持 `1 2 3`、`[1,2,3]`、`nums = [1,2,3]` 等格式）
- 第 2 行：整数 `k`

运行：
- Python：`python3 /Users/jchen/Documents/leetcode_proj/189轮转数组/rotate_array.py`
- C++：`g++ -std=c++17 /Users/jchen/Documents/leetcode_proj/189轮转数组/rotate_array.cpp -o /Users/jchen/Documents/leetcode_proj/189轮转数组/rotate_array && /Users/jchen/Documents/leetcode_proj/189轮转数组/rotate_array`

### 示例 1
- 输入：`nums = [1,2,3,4,5,6,7]`, `k = 3`
- 输出：`[5,6,7,1,2,3,4]`
- 解释：  
  - 向右轮转 1 步：`[7,1,2,3,4,5,6]`  
  - 向右轮转 2 步：`[6,7,1,2,3,4,5]`  
  - 向右轮转 3 步：`[5,6,7,1,2,3,4]`

### 示例 2
- 输入：`nums = [-1,-100,3,99]`, `k = 2`
- 输出：`[3,99,-1,-100]`
- 解释：  
  - 向右轮转 1 步：`[99,-1,-100,3]`  
  - 向右轮转 2 步：`[3,99,-1,-100]`

### 提示
- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

### 进阶
- 尽可能想出更多解决方案（至少三种）。
- 你可以使用空间复杂度为 `O(1)` 的 **原地** 算法解决这个问题吗？

---

## 核心观察
向右轮转 `k` 次等价于：每个元素 `nums[i]` 移动到新位置 `(i + k) % n`（其中 `n = len(nums)`）。

同时注意：
- `k` 可能大于 `n`，所以应先做 `k %= n`。
- 当 `k == 0` 或 `n <= 1` 时，数组不变。

---

## 解法一：额外数组（最直观）
### 思路
创建新数组 `res`，把每个元素直接放到目标位置：
- `res[(i + k) % n] = nums[i]`
最后把 `res` 覆盖回 `nums`。

### 复杂度
- 时间：`O(n)`
- 空间：`O(n)`

### Python 参考实现
```python
def rotate(nums, k):
    n = len(nums)
    if n <= 1:
        return
    k %= n
    if k == 0:
        return
    res = [0] * n
    for i, x in enumerate(nums):
        res[(i + k) % n] = x
    nums[:] = res
```

### C++ 参考实现
```cpp
void rotate(vector<int>& nums, int k) {
    int n = (int)nums.size();
    if (n <= 1) return;
    k %= n;
    if (k == 0) return;
    vector<int> res(n);
    for (int i = 0; i < n; ++i) {
        res[(i + k) % n] = nums[i];
    }
    nums = std::move(res);
}
```

---

## 解法二：三次翻转（原地 O(1)，最常用）
### 思路（最重要）
将数组向右轮转 `k`，等价于：
1. 翻转整个数组
2. 翻转前 `k` 个元素
3. 翻转后 `n-k` 个元素

为什么对？
- 假设原数组是 `[A | B]`，其中 `B` 是末尾长度为 `k` 的部分。  
  轮转结果应为 `[B | A]`。
- 整体翻转得到 `reverse([A|B]) = [reverse(B) | reverse(A)]`
- 再分别翻转两段：  
  `reverse(reverse(B)) = B`，`reverse(reverse(A)) = A`  
  最终得到 `[B | A]`。

### 复杂度
- 时间：`O(n)`（每个元素最多被交换常数次）
- 空间：`O(1)`（原地）

### Python 参考实现
```python
def rotate(nums, k):
    n = len(nums)
    if n <= 1:
        return
    k %= n
    if k == 0:
        return

    def rev(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    rev(0, n - 1)
    rev(0, k - 1)
    rev(k, n - 1)
```

### C++ 参考实现
```cpp
void rotate(vector<int>& nums, int k) {
    int n = (int)nums.size();
    if (n <= 1) return;
    k %= n;
    if (k == 0) return;
    std::reverse(nums.begin(), nums.end());
    std::reverse(nums.begin(), nums.begin() + k);
    std::reverse(nums.begin() + k, nums.end());
}
```

---

## 解法三：环状替换（Cyclic Replacements，原地 O(1)）
### 思路
根据映射 `i -> (i + k) % n`，位置会形成若干个“环”（cycle）。
从某个起点开始，把元素按环移动到目标位置；一个环结束后，从下一个未处理的位置继续，直到所有元素都移动过一次。

关键点：
- 用 `count` 统计已经放置到正确位置的元素数量，达到 `n` 就结束。
- 当走回起点时，一个环完成，换新的起点。

### 复杂度
- 时间：`O(n)`（每个元素恰好移动一次）
- 空间：`O(1)`

### Python 参考实现
```python
def rotate(nums, k):
    n = len(nums)
    if n <= 1:
        return
    k %= n
    if k == 0:
        return

    count = 0
    start = 0
    while count < n:
        cur = start
        prev = nums[start]
        while True:
            nxt = (cur + k) % n
            nums[nxt], prev = prev, nums[nxt]
            cur = nxt
            count += 1
            if cur == start:
                break
        start += 1
```

### C++ 参考实现
```cpp
void rotate(vector<int>& nums, int k) {
    int n = (int)nums.size();
    if (n <= 1) return;
    k %= n;
    if (k == 0) return;

    int count = 0;
    for (int start = 0; count < n; ++start) {
        int cur = start;
        int prev = nums[start];
        while (true) {
            int nxt = (cur + k) % n;
            std::swap(nums[nxt], prev);
            cur = nxt;
            ++count;
            if (cur == start) break;
        }
    }
}
```

---

## 如何选择
- **想最快写对**：解法一（额外数组）。
- **面试最推荐 / 进阶要求 O(1)**：解法二（三次翻转），代码短、最稳定。
- **展示更深理解**：解法三（环状替换），适合理解置换/循环结构。

---

## 常见坑
- 忘记做 `k %= n`（`k` 可能比数组长度大很多）。
- `k == 0` 时不需要操作，避免 `reverse` 边界问题。
- 环状替换如果不维护 `count`，容易死循环或漏元素。

