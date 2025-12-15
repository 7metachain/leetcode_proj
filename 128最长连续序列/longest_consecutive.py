"""
128. 最长连续序列 —— 本地可运行版本 (Python3)

输入格式（每行一组，直到 EOF 退出）：
  - [100,4,200,1,3,2]
  - 100 4 200 1 3 2
  - 100, 4, 200, 1, 3, 2

输出：最长连续序列的长度
"""

from __future__ import annotations


def longest_consecutive(nums: list[int]) -> int:
    """用 set 做 O(1) 查找，只从起点开始向右扩展"""
    s = set(nums)
    ans = 0

    for x in s:
        # 只从起点开始：x-1 不存在说明 x 是某个连续序列的最左端
        if x - 1 not in s:
            cur = x
            while cur in s:
                cur += 1
            ans = max(ans, cur - x)

    return ans


def _parse_ints(line: str) -> list[int]:
    """解析一行输入为整数列表，兼容多种格式"""
    cleaned = (
        line.replace("[", " ")
        .replace("]", " ")
        .replace(",", " ")
    )
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
        nums = _parse_ints(line)
        result = longest_consecutive(nums)
        print(result)


if __name__ == "__main__":
    main()

