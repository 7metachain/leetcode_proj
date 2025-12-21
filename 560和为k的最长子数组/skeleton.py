"""
560. 和为 K 的子数组 —— 关卡化学习骨架 (Python3)

🎯 学习目标：
   - 理解前缀和的数学变换
   - 掌握"前缀和 + 哈希表"的经典模式
   - 最终写出 O(n) 最优解

📌 使用方法：
   1. 修改 LEVEL 变量控制当前关卡 (1-6)
   2. 在 TODO (Level X) 处填写代码
   3. 运行验证：python3 skeleton.py

📌 输入格式（内置测试 + 交互式）：
   - 程序会先运行内置测试
   - 然后可输入自定义用例（每组两行：数组 和 k）
"""

from __future__ import annotations
from collections import defaultdict

# ============================================================
# 🎮 LEVEL 控制器 —— 修改这里切换关卡
# ============================================================
LEVEL = 1

# ============================================================
# 📊 统一测试用例（贯穿所有关卡）
# ============================================================
TEST_CASES = [
    # (nums, k, expected_answer)
    ([1, 1, 1], 2, 2),           # 子数组 [1,1] 出现 2 次
    ([1, 2, 3], 3, 2),           # [1,2] 和 [3]
    ([1, -1, 0], 0, 3),          # [1,-1], [-1,0,1... wait], [0], [1,-1,0] — 实际是 3
    ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4),
]


# ============================================================
# Level 1：题意建模 —— 子数组和的计算
# ============================================================
def subarray_sum_range(nums: list[int], l: int, r: int) -> int:
    """
    计算 nums[l..r] 的和（闭区间）
    
    TODO (Level 1): 用一个循环累加 nums[l] 到 nums[r] 的元素
    """
    total = 0
    # -------- 在此填写 --------
    
    # ----------------------------
    return total


# ============================================================
# Level 2：暴力解 —— 枚举所有子数组 O(n²)
# ============================================================
def brute_force(nums: list[int], k: int) -> int:
    """
    暴力解：双层循环枚举所有 (l, r) 对
    复杂度：O(n²)
    
    这是"真值函数"，后续可用于对拍验证
    """
    n = len(nums)
    ans = 0
    
    # TODO (Level 2): 枚举左端点 l，对每个 l 枚举右端点 r
    #                 用累加的方式维护 sum，避免重复计算
    # -------- 在此填写 --------
    
    # ----------------------------
    
    return ans


# ============================================================
# Level 3：中间信息暴露 —— 打印前缀和，理解等价变换
# ============================================================
def explain_prefix_sum(nums: list[int], k: int) -> None:
    """
    打印前缀和数组，帮助理解：
      sum(l, r) = pre[r] - pre[l-1]  (当 l > 0)
      sum(0, r) = pre[r]             (当 l = 0)
    
    关键洞察：
      sum(l, r) = k
      => pre[r] - pre[l-1] = k
      => pre[l-1] = pre[r] - k
      
    意思是：当右端点固定为 r 时，
    满足条件的左端点个数 = 之前出现过多少次前缀和等于 (pre[r] - k)
    """
    n = len(nums)
    
    # 计算前缀和数组（pre[i] = nums[0] + ... + nums[i]）
    pre = [0] * n
    # TODO (Level 3): 填写前缀和的递推公式
    # -------- 在此填写 --------
    
    # ----------------------------
    
    print(f"nums = {nums}, k = {k}")
    print(f"前缀和 pre = {pre}")
    print()
    
    # 展示等价变换
    print("展示 sum(l,r) = pre[r] - pre[l-1] 的等价性：")
    for l in range(n):
        for r in range(l, n):
            if l == 0:
                s = pre[r]
                formula = f"pre[{r}] = {pre[r]}"
            else:
                s = pre[r] - pre[l - 1]
                formula = f"pre[{r}] - pre[{l-1}] = {pre[r]} - {pre[l-1]} = {s}"
            if s == k:
                print(f"  ✅ sum({l},{r}) = {formula} = {k}")
    print()


# ============================================================
# Level 4-6：目标解函数 —— 前缀和 + 哈希表 O(n)
# ============================================================
def subarray_sum_optimal(nums: list[int], k: int) -> int:
    """
    最优解：前缀和 + 哈希表
    复杂度：O(n) 时间，O(n) 空间
    
    核心思想：
      cnt[s] = 前缀和 s 出现的次数
      遍历时，对于当前前缀和 prefix_sum：
        - 需要找的历史前缀和是 prefix_sum - k
        - ans += cnt[prefix_sum - k]
        - 然后 cnt[prefix_sum] += 1
    """
    # Level 4: 引入哈希表 cnt
    cnt: dict[int, int] = defaultdict(int)
    
    # TODO (Level 6): 为什么需要 cnt[0] = 1？
    #   当 prefix_sum == k 时，prefix_sum - k == 0
    #   cnt[0] = 1 表示"空前缀"出现 1 次
    #   这样才能正确统计从下标 0 开始的子数组
    # -------- 在此填写 --------
    
    # ----------------------------
    
    prefix_sum = 0
    ans = 0
    
    for x in nums:
        prefix_sum += x
        
        # TODO (Level 5): 统计之前出现过多少次 prefix_sum - k
        # -------- 在此填写 --------
        
        # ----------------------------
        
        # TODO (Level 5): 记录当前前缀和出现次数
        # -------- 在此填写 --------
        
        # ----------------------------
    
    return ans


# ============================================================
# 🧪 测试入口
# ============================================================
def run_tests() -> None:
    """运行内置测试用例"""
    print(f"{'='*60}")
    print(f"🎮 当前关卡：Level {LEVEL}")
    print(f"{'='*60}\n")
    
    if LEVEL == 1:
        print("📌 Level 1：题意建模 —— 实现 subarray_sum_range(nums, l, r)")
        print("   目标：计算 nums[l..r] 的和\n")
        
        nums = [1, 2, 3, 4, 5]
        print(f"nums = {nums}")
        print(f"subarray_sum_range(nums, 0, 2) = {subarray_sum_range(nums, 0, 2)}  (期望: 6)")
        print(f"subarray_sum_range(nums, 1, 3) = {subarray_sum_range(nums, 1, 3)}  (期望: 9)")
        print(f"subarray_sum_range(nums, 2, 4) = {subarray_sum_range(nums, 2, 4)}  (期望: 12)")
    
    elif LEVEL == 2:
        print("📌 Level 2：暴力解 —— 双层循环枚举所有 (l, r) 对")
        print("   目标：实现 O(n²) 的暴力解\n")
        
        for nums, k, expected in TEST_CASES:
            result = brute_force(nums, k)
            status = "✅" if result == expected else "❌"
            print(f"{status} brute_force({nums}, {k}) = {result}  (期望: {expected})")
    
    elif LEVEL == 3:
        print("📌 Level 3：中间信息暴露 —— 理解前缀和等价变换")
        print("   目标：实现前缀和递推，观察 sum(l,r) = pre[r] - pre[l-1]\n")
        
        explain_prefix_sum([1, 1, 1], 2)
        explain_prefix_sum([1, 2, 3], 3)
    
    elif LEVEL >= 4:
        level_desc = {
            4: "Level 4：解法结构骨架 —— 引入哈希表 cnt",
            5: "Level 5：关键思想注入 —— 填写核心逻辑",
            6: "Level 6：最优解完成 —— 理解 cnt[0] = 1 的必要性",
        }
        print(f"📌 {level_desc.get(LEVEL, level_desc[6])}\n")
        
        all_pass = True
        for nums, k, expected in TEST_CASES:
            result = subarray_sum_optimal(nums, k)
            status = "✅" if result == expected else "❌"
            if result != expected:
                all_pass = False
            print(f"{status} subarray_sum_optimal({nums}, {k}) = {result}  (期望: {expected})")
        
        if all_pass and LEVEL == 6:
            print("\n🎉 恭喜！所有测试通过，你已完成最优解！")
            print("   现在可以删除 LEVEL 相关代码，骨架即为最终答案。")


def interactive_mode() -> None:
    """交互模式：输入自定义测试"""
    import sys
    
    print("\n" + "="*60)
    print("📝 交互模式：输入自定义测试（Ctrl+D 退出）")
    print("   格式：第1行 数组（如 [1,1,1]），第2行 整数 k")
    print("="*60 + "\n")
    
    try:
        lines = sys.stdin.read().splitlines()
    except KeyboardInterrupt:
        return
    
    i = 0
    while i + 1 < len(lines):
        nums_line = lines[i].strip()
        k_line = lines[i + 1].strip()
        if nums_line and k_line:
            nums = _parse_ints(nums_line)
            k = int(k_line)
            
            if LEVEL <= 2:
                result = brute_force(nums, k)
                print(f"brute_force({nums}, {k}) = {result}")
            else:
                result = subarray_sum_optimal(nums, k)
                print(f"subarray_sum_optimal({nums}, {k}) = {result}")
        i += 2


def _parse_ints(line: str) -> list[int]:
    """解析一行输入为整数列表"""
    cleaned = line.replace("[", " ").replace("]", " ").replace(",", " ")
    return [int(tok) for tok in cleaned.split() if tok.lstrip("-").isdigit()]


if __name__ == "__main__":
    run_tests()
    # 如需交互测试，取消下面注释
    # interactive_mode()

