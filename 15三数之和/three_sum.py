"""
15. 三数之和 —— 本地可运行版本 (Python3)

输入格式（每行一组，直到 EOF 退出）：
  - [-1,0,1,2,-1,-4]
  - -1 0 1 2 -1 -4
  - -1, 0, 1, 2, -1, -4

输出：所有不重复的三元组，如 [[-1,-1,2],[-1,0,1]]
"""

from __future__ import annotations


def three_sum(nums: list[int]) -> list[list[int]]:
    """排序 + 固定一个数 + 双指针 + 去重，O(n²) 时间"""
    nums.sort()
    n = len(nums)
    result: list[list[int]] = []

    for i in range(n - 2):
        # 剪枝：排序后如果 nums[i] > 0，后面全是正数，不可能凑出 0
        if nums[i] > 0:
            break
        # i 去重
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, n - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                # l 去重
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                # r 去重
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1

    return result


def _parse_ints(line: str) -> list[int]:
    """解析一行输入为整数列表，兼容多种格式"""
    cleaned = line.replace("[", " ").replace("]", " ").replace(",", " ")
    out: list[int] = []
    for tok in cleaned.split():
        try:
            out.append(int(tok))
        except ValueError:
            continue
    return out


def _format_output(triplets: list[list[int]]) -> str:
    """格式化输出"""
    inner = ",".join("[" + ",".join(str(x) for x in t) + "]" for t in triplets)
    return "[" + inner + "]"


def main() -> None:
    import sys

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        nums = _parse_ints(line)
        result = three_sum(nums)
        print(_format_output(result))


if __name__ == "__main__":
    main()

