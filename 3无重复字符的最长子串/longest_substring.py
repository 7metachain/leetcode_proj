"""
3. 无重复字符的最长子串 —— 本地可运行版本 (Python3)

输入格式（每行一个字符串，直到 EOF 退出）：
  - abcabcbb
  - pwwkew

输出：最长子串长度 及 子串本身
"""

from __future__ import annotations


def length_of_longest_substring(s: str) -> tuple[int, str]:
    """滑动窗口 + last 字典，O(n) 时间"""
    last: dict[str, int] = {}
    left = 0
    best_left = 0
    best_len = 0

    for right, c in enumerate(s):
        if c in last:
            # left 只能往右，不能往回
            left = max(left, last[c] + 1)

        last[c] = right
        cur_len = right - left + 1

        if cur_len > best_len:
            best_len = cur_len
            best_left = left

    return best_len, s[best_left : best_left + best_len]


def main() -> None:
    import sys

    for line in sys.stdin:
        s = line.strip()
        if not s:
            continue
        length, substring = length_of_longest_substring(s)
        print(f'{length} "{substring}"')


if __name__ == "__main__":
    main()

