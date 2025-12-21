"""
560. 和为 K 的子数组 —— 本地可运行版本 (Python3)

输入格式（每组两行，直到 EOF 退出）：
  第 1 行：数组 nums（如 [1,1,1] 或 1 1 1）
  第 2 行：整数 k

输出：和为 k 的连续子数组个数
"""

from __future__ import annotations
from collections import defaultdict


def subarray_sum(nums: list[int], k: int) -> int:
    """前缀和 + 哈希表，O(n) 时间"""
    cnt: dict[int, int] = defaultdict(int)
    cnt[0] = 1  # 空前缀：前缀和为 0 出现 1 次

    prefix_sum = 0
    ans = 0

    for x in nums:
        prefix_sum += x
        # 统计之前出现过多少次 prefix_sum - k
        ans += cnt[prefix_sum - k]
        # 记录当前前缀和
        cnt[prefix_sum] += 1

    return ans


def _parse_ints(line: str) -> list[int]:
    """解析一行输入为整数列表"""
    cleaned = line.replace("[", " ").replace("]", " ").replace(",", " ")
    out: list[int] = []
    for tok in cleaned.split():
        try:
            out.append(int(tok))
        except ValueError:
            continue
    return out


def main() -> None:
    import sys

    lines = sys.stdin.read().splitlines()
    i = 0
    while i + 1 < len(lines):
        nums_line = lines[i].strip()
        k_line = lines[i + 1].strip()
        if nums_line and k_line:
            nums = _parse_ints(nums_line)
            k = int(k_line)
            result = subarray_sum(nums, k)
            print(result)
        i += 2


if __name__ == "__main__":
    main()

