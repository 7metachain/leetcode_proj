"""
11. 盛最多水的容器 —— 本地可运行版本 (Python3)

输入格式（每行一组，直到 EOF 退出）：
  - [1,8,6,2,5,4,8,3,7]
  - 1 8 6 2 5 4 8 3 7
  - 1, 8, 6, 2, 5, 4, 8, 3, 7

输出：最大盛水面积
"""

from __future__ import annotations


def max_area(height: list[int]) -> int:
    """双指针，O(n) 时间"""
    l, r = 0, len(height) - 1
    ans = 0

    while l < r:
        h = min(height[l], height[r])
        w = r - l
        ans = max(ans, h * w)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return ans


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


def main() -> None:
    import sys

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        height = _parse_ints(line)
        if len(height) < 2:
            print(0)
            continue
        result = max_area(height)
        print(result)


if __name__ == "__main__":
    main()

