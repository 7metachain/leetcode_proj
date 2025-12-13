# 1. 两数之和（Two Sum）笔记

## 本地可运行版本（Python / C++）
本目录提供两份可直接运行的程序（默认使用“单循环一次遍历”写法）：
- `two_sum.py`
- `two_sum.cpp`

输入格式（可重复多组，直到 EOF 结束）：
- 第 1 行：数组 `nums`（支持 `2 7 11 15`、`[2,7,11,15]`、`nums = [2,7,11,15]`）
- 第 2 行：整数 `target`（支持 `9` 或 `target = 9`）

输出格式：`[i,j]`（两个下标）。

运行：
- Python：`python3 /Users/jchen/Documents/leetcode_proj/1两数之和/two_sum.py`
- C++：`g++ -std=c++17 /Users/jchen/Documents/leetcode_proj/1两数之和/two_sum.cpp -o /Users/jchen/Documents/leetcode_proj/1两数之和/two_sum && /Users/jchen/Documents/leetcode_proj/1两数之和/two_sum`

切换为“双循环两次遍历”版本（可选）：
- Python：`TWOSUM_METHOD=two python3 /Users/jchen/Documents/leetcode_proj/1两数之和/two_sum.py`
- C++：`TWOSUM_METHOD=two /Users/jchen/Documents/leetcode_proj/1两数之和/two_sum`

## 一、单循环（一次遍历）写法

👉 官方 / 高频写法

### 核心思想（一句话）
遍历到当前位置 `i`（较大的下标），用哈希表去“回头找”是否存在匹配的较小下标。

### C++（单循环）
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp; // 数值 -> 下标

        for (int i = 0; i < nums.size(); i++) {
            int need = target - nums[i];
            if (mp.count(need)) {
                return {mp[need], i};
            }
            mp[nums[i]] = i;
        }
        return {};
    }
};
```

### Python3（单循环）
```python
class Solution:
    def twoSum(self, nums, target):
        mp = {}  # 数值 -> 下标

        for i, x in enumerate(nums):
            need = target - x
            if need in mp:
                return [mp[need], i]
            mp[x] = i
```

### 这个写法的“真实执行顺序”
- 先遇到答案中下标更大的那个元素
- 再通过哈希表，回头找到下标更小的那个元素

这正是你觉得它“不直观”的原因。

## 二、双循环（两次遍历）写法

👉 你更认可、也更符合人类直觉的写法

### 核心思想（一句话）
先掌握全局信息（建表），再做判断（匹配）。

### Python3（双循环）
```python
class Solution:
    def twoSum(self, nums, target):
        mp = {}

        # 第一遍：建立哈希表
        for i, x in enumerate(nums):
            mp[x] = i

        # 第二遍：查找配对
        for i, x in enumerate(nums):
            need = target - x
            if need in mp and mp[need] != i:
                return [i, mp[need]]
```

### C++（双循环）
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp;

        // 第一遍：建表
        for (int i = 0; i < nums.size(); i++) {
            mp[nums[i]] = i;
        }

        // 第二遍：查找
        for (int i = 0; i < nums.size(); i++) {
            int need = target - nums[i];
            if (mp.count(need) && mp[need] != i) {
                return {i, mp[need]};
            }
        }
        return {};
    }
};
```

## 复杂度（你说得完全对）
- 时间复杂度：O(n) + O(n) = O(n)
- 空间复杂度：O(n)
- 和单循环在复杂度上完全等价。