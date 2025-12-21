"""
15. 三数之和 —— 关卡化学习骨架 (Python)

🎯 总目标：通过逐步填空，最终自然写出最优解

关卡顺序：
  Level 1: 题意建模 —— 实现 three_sum(i, j, k) 计算三数和
  Level 2: 暴力正确解 —— O(n³) 穷举所有三元组（允许重复）
  Level 3: 中间信息暴露 —— 打印找到的三元组，观察重复问题
  Level 4: 双指针骨架 —— 排序 + 固定 i + 双指针框架（移动规则留空）
  Level 5: 移动规则注入 —— 填写 s < 0 / s > 0 时的移动
  Level 6: 去重规则 —— 加入 i 去重 和 l/r 去重
  Level 7: 最优解完成 —— 加入剪枝，整合代码

使用方法：
  1. 修改 LEVEL 变量控制当前关卡
  2. 在对应的 TODO 位置填写代码
  3. 运行验证：python3 skeleton.py
"""

# ========================================
# 🎮 LEVEL 控制器（修改这里切换关卡）
# ========================================
LEVEL = 1  # 当前关卡：1, 2, 3, 4, 5, 6, 7

# ========================================
# 📊 测试数据（所有关卡共用）
# ========================================
TEST_NUMS = [-1, 0, 1, 2, -1, -4]
# 期望答案（不重复的三元组）：[[-1, -1, 2], [-1, 0, 1]]
EXPECTED_ANS = [[-1, -1, 2], [-1, 0, 1]]


# ========================================
# 🧱 Level 1: 题意建模 —— three_sum 函数
# ========================================
def three_sum(nums: list[int], i: int, j: int, k: int) -> int:
    """
    计算 nums[i] + nums[j] + nums[k]

    TODO (Level 1): 实现这个函数（1 行代码）
    """
    # ↓↓↓ 在下面填写你的代码 ↓↓↓
    pass  # 删掉 pass，写出正确的 return 语句
    # ↑↑↑ 在上面填写你的代码 ↑↑↑


# ========================================
# 🧱 Level 2: 暴力正确解 —— O(n³)
# ========================================
def solve_brute_force(nums: list[int]) -> list[list[int]]:
    """
    暴力穷举所有 (i, j, k) 组合，找出和为 0 的三元组
    注意：这一关允许有重复，先把题意做对

    TODO (Level 2): 用三层循环穷举，调用 three_sum
    提示：i < j < k
    """
    n = len(nums)
    result = []

    # ↓↓↓ 在下面填写你的代码（约 5-6 行）↓↓↓
    pass  # 删掉 pass，写出三重循环
    # ↑↑↑ 在上面填写你的代码 ↑↑↑

    return result


# ========================================
# 🧱 Level 3: 中间信息暴露 —— 观察重复
# ========================================
def solve_brute_force_verbose(nums: list[int]) -> list[list[int]]:
    """
    和 Level 2 一样，但打印每个找到的三元组
    观察：哪些三元组是重复的？

    TODO (Level 3): 复制 Level 2 代码，加上 print 语句
    """
    n = len(nums)
    result = []

    # ↓↓↓ 在下面填写你的代码 ↓↓↓
    pass  # 删掉 pass
    # ↑↑↑ 在上面填写你的代码 ↑↑↑

    print(f"[Level 3] 共找到 {len(result)} 个三元组（可能有重复）")
    return result


# ========================================
# 🧱 Level 4: 双指针骨架 —— 框架搭建
# ========================================
def solve_two_pointers_skeleton(nums: list[int]) -> list[list[int]]:
    """
    双指针框架：
      1. 先排序
      2. 固定 i，在 [i+1, n-1] 区间用双指针
      3. 移动规则暂时留空（直接 break）

    TODO (Level 4): 填写排序 + 外层循环 + 双指针初始化
    """
    nums = sorted(nums)  # 排序（不修改原数组）
    n = len(nums)
    result = []

    # ↓↓↓ 在下面填写你的代码（约 6-8 行）↓↓↓
    # 提示：for i in range(n - 2)
    # 提示：l = i + 1, r = n - 1
    # 提示：while l < r: ... 暂时只计算 s，然后 break
    pass  # 删掉 pass
    # ↑↑↑ 在上面填写你的代码 ↑↑↑

    return result


# ========================================
# 🧱 Level 5: 移动规则注入
# ========================================
def solve_two_pointers_move(nums: list[int]) -> list[list[int]]:
    """
    核心移动规则（排序后）：
      - s == 0：找到答案，l++, r--
      - s < 0：和太小，l++（让和变大）
      - s > 0：和太大，r--（让和变小）

    TODO (Level 5): 填写 if-elif-else 移动规则
    注意：这一关还没有去重，结果可能有重复
    """
    nums = sorted(nums)
    n = len(nums)
    result = []

    for i in range(n - 2):
        l, r = i + 1, n - 1

        while l < r:
            s = nums[i] + nums[l] + nums[r]

            # ↓↓↓ 在下面填写移动规则（约 8-10 行）↓↓↓
            # 提示：if s == 0: 记录答案，l += 1, r -= 1
            # 提示：elif s < 0: l += 1
            # 提示：else: r -= 1
            pass  # 删掉 pass
            # ↑↑↑ 在上面填写你的代码 ↑↑↑

    return result


# ========================================
# 🧱 Level 6: 去重规则
# ========================================
def solve_two_pointers_dedup(nums: list[int]) -> list[list[int]]:
    """
    去重规则（最容易 WA 的点）：

    1️⃣ i 的去重：
       if i > 0 and nums[i] == nums[i - 1]: continue

    2️⃣ 找到一组解后的 l/r 去重：
       while l < r and nums[l] == nums[l - 1]: l += 1
       while l < r and nums[r] == nums[r + 1]: r -= 1

    TODO (Level 6): 在 Level 5 基础上加入去重
    """
    nums = sorted(nums)
    n = len(nums)
    result = []

    for i in range(n - 2):
        # ↓↓↓ 在下面加入 i 的去重（1 行）↓↓↓
        pass  # 删掉 pass
        # ↑↑↑ i 去重 ↑↑↑

        l, r = i + 1, n - 1

        while l < r:
            s = nums[i] + nums[l] + nums[r]

            if s == 0:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1

                # ↓↓↓ 在下面加入 l/r 的去重（2 行）↓↓↓
                pass  # 删掉 pass
                # ↑↑↑ l/r 去重 ↑↑↑

            elif s < 0:
                l += 1
            else:
                r -= 1

    return result


# ========================================
# 🧱 Level 7: 最优解完成（加入剪枝）
# ========================================
def solve_optimal(nums: list[int]) -> list[list[int]]:
    """
    最终最优解：排序 + 固定 i + 双指针 + 去重 + 剪枝
    时间 O(n²)，空间 O(1)（不计输出）

    剪枝：if nums[i] > 0: break
    （排序后，如果 nums[i] > 0，后面全是正数，不可能凑出 0）

    TODO (Level 7): 整合 Level 6，加入剪枝
    """
    nums = sorted(nums)
    n = len(nums)
    result = []

    # ↓↓↓ 完整的最优解代码 ↓↓↓
    pass  # 删掉 pass
    # ↑↑↑ 完整的最优解代码 ↑↑↑

    return result


# ========================================
# 🧪 辅助函数：比较两个结果是否等价
# ========================================
def normalize(triplets: list[list[int]]) -> set[tuple[int, ...]]:
    """把三元组列表转成 set，用于比较（忽略顺序）"""
    return set(tuple(sorted(t)) for t in triplets)


# ========================================
# 🧪 统一测试入口
# ========================================
def main():
    print("=" * 60)
    print(f"🎮 当前关卡: Level {LEVEL}")
    print(f"📊 测试数据: {TEST_NUMS}")
    print(f"✅ 期望答案: {EXPECTED_ANS}")
    print("=" * 60)

    result = None

    if LEVEL == 1:
        # 测试 three_sum 函数
        # nums = [-1, 0, 1, 2, -1, -4]
        # three_sum(nums, 0, 1, 2) = -1 + 0 + 1 = 0
        test_sum = three_sum(TEST_NUMS, 0, 1, 2)
        expected_sum = TEST_NUMS[0] + TEST_NUMS[1] + TEST_NUMS[2]
        print(f"[Level 1] three_sum(nums, 0, 1, 2) = {test_sum}")
        print(f"[Level 1] 期望值 = {expected_sum}")
        if test_sum == expected_sum:
            print("✅ Level 1 通过！可以进入 Level 2")
        else:
            print("❌ Level 1 未通过，请检查 three_sum 函数")

    elif LEVEL == 2:
        result = solve_brute_force(TEST_NUMS)
        print(f"[Level 2] 暴力解结果: {result}")

    elif LEVEL == 3:
        result = solve_brute_force_verbose(TEST_NUMS)
        print(f"[Level 3] 暴力解(verbose)结果: {result}")

    elif LEVEL == 4:
        result = solve_two_pointers_skeleton(TEST_NUMS)
        print(f"[Level 4] 双指针骨架结果: {result}")

    elif LEVEL == 5:
        result = solve_two_pointers_move(TEST_NUMS)
        print(f"[Level 5] 双指针+移动规则结果: {result}")
        print("  ⚠️ 注意：这一关还没有去重，结果可能有重复")

    elif LEVEL == 6:
        result = solve_two_pointers_dedup(TEST_NUMS)
        print(f"[Level 6] 双指针+去重结果: {result}")

    elif LEVEL == 7:
        result = solve_optimal(TEST_NUMS)
        print(f"[Level 7] 最优解结果: {result}")

    # 验证结果
    if result is not None and LEVEL >= 2:
        result_set = normalize(result)
        expected_set = normalize(EXPECTED_ANS)

        # Level 2-5 允许有重复，只检查是否包含期望答案
        if LEVEL <= 5:
            if expected_set.issubset(result_set):
                print(f"✅ Level {LEVEL} 通过（包含所有期望答案）！")
                if LEVEL < 7:
                    print(f"👉 可以进入 Level {LEVEL + 1}")
            else:
                missing = expected_set - result_set
                print(f"❌ Level {LEVEL} 未通过，缺少: {missing}")
        else:
            # Level 6-7 要求完全匹配（无重复）
            if result_set == expected_set:
                print(f"✅ Level {LEVEL} 通过！")
                if LEVEL < 7:
                    print(f"👉 可以进入 Level {LEVEL + 1}")
                else:
                    print("🎉 恭喜！你已完成所有关卡，得到了最优解！")
            else:
                extra = result_set - expected_set
                missing = expected_set - result_set
                if extra:
                    print(f"❌ 多余的三元组: {extra}")
                if missing:
                    print(f"❌ 缺少的三元组: {missing}")


if __name__ == "__main__":
    main()

